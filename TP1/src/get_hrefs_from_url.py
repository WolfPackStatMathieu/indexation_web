import requests
from bs4 import BeautifulSoup
import urllib.robotparser
from robot import robots_entre
from urllib.parse import  urlparse, urlunparse
from get_url_base import *

def get_hrefs_from_url(url):
    """Récupère tous les liens (hrefs) d'une page.

    Args:
        url (str): L'URL de la page.

    Returns:
        set: Un ensemble de liens (hrefs) présents sur l'url fournie.
    """
    all_hrefs = set()

    try:
        # récupération du code HTML
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        # récupération des links
        href_tags = soup.find_all('a', href=True)

        for href_tag in href_tags:
            href = href_tag['href']
            all_hrefs.add(href)
            

    except requests.exceptions.RequestException as e:
        print(f"Error during request to {url}: {e}")

    return all_hrefs

if __name__ == '__main__':
    # Liste d'URLs à traiter
    url = "https://ensai.fr"

    all_hrefs = get_hrefs_from_url(url)
    for href in all_hrefs:
        print(href)