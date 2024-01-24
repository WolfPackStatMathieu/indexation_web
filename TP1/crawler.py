import concurrent.futures
import requests
from bs4 import BeautifulSoup
import urllib.robotparser
from urllib.parse import urlparse, urlunparse

# Fonction pour récupérer le contenu d'une URL
def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

# Fonction pour extraire les liens d'une page HTML avec les nouvelles conditions
def extract_links(html, max_links=2):
    links = []
    soup = BeautifulSoup(html, 'html.parser')

    # Fonction pour vérifier l'autorisation dans le fichier robots.txt pour une URL de base
    def is_allowed_by_robots(url):
        # Extrait la partie de base de l'URL (sans le chemin spécifique)
        parsed_url = urlparse(url)
        base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
        
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(base_url + "/robots.txt")
        rp.read()
        print(f'le site {url} est autorisé: {rp.can_fetch("*", url)}')
        return rp.can_fetch("*", url)

    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        # Vérifie si la taille maximale de liens n'est pas atteinte et si le lien est autorisé par le fichier robots.txt
        if len(links) < max_links and is_allowed_by_robots(link):
            links.append(link)
    return links

# Fonction pour crawler une URL avec une vérification de la taille maximale d'URL autorisées
def crawl_url(url):
    print(f"Crawling: {url}")
    html_content = fetch_url(url)
    if html_content:
        links = extract_links(html_content)
        print(f"Found {len(links)} links on {url}")
        # Vous pouvez ajouter ici la logique pour traiter les liens, les stocker, etc.
        return links
    return []

# Fonction principale pour exécuter le crawler avec plusieurs threads
def run_crawler(seed_url, max_threads=5, max_allowed_urls=5):
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

        # Affiche le nombre d'URL autorisées et les URL en question
        print(f"\nNombre d'URL autorisées visitées : {num_allowed_urls}")
        print("Liste des URL autorisées visitées :")
        for url in visited_urls:
            print(url)

if __name__ == "__main__":
    seed_url = "http://www.ensai.fr"
    visited_urls = set()

    run_crawler(seed_url)
