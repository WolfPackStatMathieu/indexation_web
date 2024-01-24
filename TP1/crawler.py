import concurrent.futures
import requests
from bs4 import BeautifulSoup
import urllib.robotparser

# Fonction pour récupérer le contenu d'une URL
def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

# Fonction pour extraire les liens d'une page HTML
# Fonction pour extraire les liens d'une page HTML avec les nouvelles conditions
def extract_links(html, max_links=5):
    links = []
    soup = BeautifulSoup(html, 'html.parser')

    # Vérifie le fichier robots.txt pour l'autorisation de l'URL
    def is_allowed_by_robots(url):
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(url + "/robots.txt")
        rp.read()
        return rp.can_fetch("*", url)

    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        # Vérifie si la taille maximale de liens n'est pas atteinte et si le lien est autorisé par le fichier robots.txt
        if len(links) < max_links and is_allowed_by_robots(link):
            links.append(link)
    return links

# Fonction pour crawler une URL
def crawl_url(url):
    print(f"Crawling: {url}")
    html_content = fetch_url(url)
    if html_content:
        links = extract_links(html_content)
        print(f"Found {len(links)} links on {url}")
        # Vous pouvez ajouter ici la logique pour traiter les liens, les stocker, etc.

# Fonction principale pour exécuter le crawler avec plusieurs threads
def run_crawler(seed_url, max_threads=5, max_allowed_urls=50):
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        # Lance le crawling pour la seed URL
        executor.submit(crawl_url, seed_url)

        # Compteur d'URL autorisées
        num_allowed_urls = 0

        # Récupère et traite les futures (résultats des tâches)
        futures = set()
        while futures or num_allowed_urls < max_allowed_urls:
            done, futures = concurrent.futures.wait(
                futures, timeout=0.1, return_when=concurrent.futures.FIRST_COMPLETED
            )
            for future in done:
                new_links = future.result()
                if new_links:
                    # Ajoute les nouvelles URLs à crawler
                    for link in new_links:
                        if link not in visited_urls and num_allowed_urls < max_allowed_urls:
                            visited_urls.add(link)
                            num_allowed_urls += 1
                            future = executor.submit(crawl_url, link)
                            futures.add(future)

if __name__ == "__main__":
    seed_url = "http://www.ensai.fr"
    visited_urls = set()

    run_crawler(seed_url)
