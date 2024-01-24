import time 
import concurrent.futures
import requests
from bs4 import BeautifulSoup
import urllib.robotparser
from urllib.parse import urlparse, urlunparse
from queue import Queue

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
def extract_links(html, max_links=5):
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
        print(link)
        # Vérifie si la taille maximale de liens n'est pas atteinte et si le lien est autorisé par le fichier robots.txt
        print(len(links))
        is_allowed = is_allowed_by_robots(link)
        if is_allowed:
            if len(links) < max_links:
                
                links.append(link)
            else:
                print(f'les liens autorisés sur {url} sont :{links}')
                return links
    return links

# Fonction pour crawler une URL avec une vérification de la taille maximale d'URL autorisées
def crawl_url(url):
    print(f"Crawling: {url}")
    html_content = fetch_url(url)
    if html_content:
        print("ENTRE DANS EXTRACT_LINKS()")
        links = extract_links(html_content)
        print(f"Found {len(links)} links on {url}")
        # Vous pouvez ajouter ici la logique pour traiter les liens, les stocker, etc.
        time.sleep(3)
        return links
    return []




# Fonction principale pour exécuter le crawler avec plusieurs threads
def run_crawler(seed_url, max_threads=5, max_allowed_urls=50):
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        # Initialise la frontière avec la seed URL
        frontier = Queue()
        frontier.put(seed_url)

        # Initialise la liste des URL de base déjà explorées
        explored_base_urls = set()

        # Compteur d'URL autorisées
        num_allowed_urls = 0

        # Récupère et traite les futures (résultats des tâches)
        futures = set()
        while not frontier.empty() and (futures or num_allowed_urls < max_allowed_urls):
            # Récupère l'URL suivante de la frontière
            current_url = frontier.get()

            # Vérifie si l'URL de base a déjà été explorée
            base_url = urlparse(current_url).scheme + "://" + urlparse(current_url).netloc
            if base_url in explored_base_urls:
                continue  # Passe à l'URL suivante si elle a déjà été explorée

            # Lance le crawling pour l'URL actuelle
            future = executor.submit(crawl_url, current_url)
            futures.add(future)

            # Ajoute l'URL de base à la liste des explorées
            explored_base_urls.add(base_url)

            # Récupère et traite les futures (résultats des tâches)
            done, futures = concurrent.futures.wait(
                futures, timeout=0.1, return_when=concurrent.futures.FIRST_COMPLETED
            )

            # Sort de la boucle s'il n'y a plus de futures à attendre
            if not done:
                break

            for future in done:
                new_links = future.result()
                if new_links:
                    # Ajoute les nouvelles URLs à la frontière
                    for link in new_links:
                        frontier.put(link)
                        num_allowed_urls += 1

        # Affiche le nombre d'URL autorisées et les URL en question
        print(f"\nNombre d'URL autorisées visitées : {num_allowed_urls}")
        print("Liste des URL autorisées visitées :")
        for url in visited_urls:
            print(url)

if __name__ == "__main__":
    seed_url = "http://www.ensai.fr"
    visited_urls = set()

    run_crawler(seed_url)
