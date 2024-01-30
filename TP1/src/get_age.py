import requests
from bs4 import BeautifulSoup
from http.client import IncompleteRead
import sys
sys.path.append("..")
from src.get_url_base import get_url_base
from src.get_urls_recursively import get_urls_recursively
from src.get_url_sitemap_index import get_url_sitemap_index
import datetime

def get_last_modified_date_of_url(url_input):
    """retourne la date de dernière modification d'une url

    Args:
        url_input (string): adresse url

    Returns:
        date: date de dernière modification, now() si non trouvée
    """
    base_url = get_url_base(url_input)
    sitemap_url = get_url_sitemap_index(base_url)
    all_urls_with_dates = get_urls_recursively(sitemap_url)
    
    if not url_input.endswith('/'):
        url_input += '/'
    for url, last_modified in all_urls_with_dates:
        if url == url_input:
            date = datetime.datetime.strptime(last_modified, "%Y-%m-%dT%H:%M:%S%z")
            return date
    print(f"Date de dernière modification non trouvée pour l'URL {url_input} spécifiée.")
    
    return datetime.datetime.now()


if __name__ == '__main__':
    url = "https://ensai.fr/"
    last_modified_date = get_last_modified_date_of_url(url)
    print(f"Date de dernière modification pour {url} : {last_modified_date}")
    print(type(last_modified_date))