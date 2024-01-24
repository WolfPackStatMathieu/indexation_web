import requests
from bs4 import BeautifulSoup
import urllib.robotparser
from robot import robots_entre
from urllib.parse import  urlparse, urlunparse

def get_hrefs_from_url(url):
    """Récupère tous les liens (hrefs) d'une page en vérifiant les règles du fichier robots.txt.

    Args:
        url (str): L'URL de la page.

    Returns:
        set: Un ensemble de liens (hrefs) autorisés par le robots.txt.
    """
    allowed_hrefs = set()

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        href_tags = soup.find_all('a', href=True)

        parsed_url = urlparse(url)

        for href_tag in href_tags:
            href = href_tag['href']
            # TODO faire une liste d'url autorisées et interdites, vérifier si l'url est 
            # déjà dedans avant d'interroger le robot de l'url de base
            absolute_href = urljoin(url, href)
            parsed_href = urlparse(absolute_href)

            # Vérifier si l'URL est autorisée par le robots.txt et n'est pas déjà présente dans allowed_hrefs
            if robots_entre(absolute_href) and absolute_href not in allowed_hrefs:
                allowed_hrefs.add(absolute_href)

    except requests.exceptions.RequestException as e:
        print(f"Error during request to {url}: {e}")

    return allowed_hrefs

if __name__ == '__main__':
    # Liste d'URLs à traiter
    all_urls_recursively = ["https://example.com/page1", "https://example.com/page2", ...]

    # Ensemble pour stocker tous les href autorisés
    all_allowed_hrefs = set()

    for url in all_urls_recursively:
        hrefs = get_hrefs_from_url(url)
        all_allowed_hrefs.update(hrefs)

    # Afficher les href autorisés
    print("Href autorisés :")
    for href in all_allowed_hrefs:
        print(href)