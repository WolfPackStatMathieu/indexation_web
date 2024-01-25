import requests
from bs4 import BeautifulSoup
from http.client import IncompleteRead
import sys
sys.path.append("..")
from src.get_url_base import get_url_base
from src.get_urls_recursively import get_urls_recursively



def get_last_modified_date_of_url(url):
    base_url = get_url_base(url)
    all_urls_with_dates = get_urls_recursively(sitemap_url)
    
    for url, last_modified in all_urls_with_dates:
        if url == base_url:
            return last_modified
    
    return "Date de dernière modification non trouvée pour l'URL spécifiée."


if __name__ == '__main__':
    base_url = "https://ensai.fr/"
    sitemap_url = base_url + "sitemap_index.xml"

    last_modified_date = get_last_modified_date_of_url(sitemap_url, base_url)
    print(f"Date de dernière modification pour {base_url} : {last_modified_date}")