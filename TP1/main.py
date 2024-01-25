from bs4 import BeautifulSoup
import urllib.request
from src import retourner_html
from src.get_urls_recursively import *

###### phase d'initialisation ######
# lecture du site Ensai.fr
url_base ='https://ensai.fr'
# récupération de toutes les pages du site
url_base_sitemap = url_base + "/sitemap_index.xml"
all_urls_recursively = get_urls_recursively(url_base_sitemap)
print(all_urls_recursively)
# pseudo code:
# fonction récupérer_links_d'un_site(liste: liste des url d'un site): Return: liste: liste des links autorisées
# pour chaque page on va récupérer les urls:
# links_autorisés = []
# links_interdits = []

# pour chaque url dans all_url_recursively FAIRE
#   liste_href    



