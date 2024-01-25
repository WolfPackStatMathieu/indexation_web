import requests
from bs4 import BeautifulSoup
from http.client import IncompleteRead
import sys
sys.path.append("..")
from get_url_base import get_url_base
from get_urls_recursively import get_urls_recursively


def get_last_modified_date_of_url(url_input):
    base_url = get_url_base(url_input)
    sitemap_url = base_url + "/sitemap_index.xml"
    all_urls_with_dates = get_urls_recursively(sitemap_url)
    
    for url, last_modified in all_urls_with_dates:
        if url == url_input:
            return last_modified
    
    return "Date de dernière modification non trouvée pour l'URL spécifiée."


if __name__ == '__main__':
    url = "https://ensai.fr/"
    last_modified_date = get_last_modified_date_of_url(url)
    print(f"Date de dernière modification pour {url} : {last_modified_date}")