import requests
from bs4 import BeautifulSoup
from http.client import IncompleteRead
import sys
sys.path.append("..")
from get_url_base import get_url_base
from get_urls_recursively import get_urls_recursively
from get_url_sitemap_index import get_url_sitemap_index

def get_last_modified_date_of_url(url_input):
    """retourne la date de dernière modification d'une url

    Args:
        url_input (string): adresse url

    Returns:
        date: date de dernière modification
    """
    base_url = get_url_base(url_input)
    sitemap_url = get_url_sitemap_index(base_url)
    all_urls_with_dates = get_urls_recursively(sitemap_url)
    
    for url, last_modified in all_urls_with_dates:
        if url == url_input:
            return last_modified
    
    return "Date de dernière modification non trouvée pour l'URL spécifiée."


if __name__ == '__main__':
    url = "https://ensai.fr/"
    last_modified_date = get_last_modified_date_of_url(url)
    print(f"Date de dernière modification pour {url} : {last_modified_date}")