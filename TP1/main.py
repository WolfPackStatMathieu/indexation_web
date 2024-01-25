from bs4 import BeautifulSoup
import urllib.request
from src import retourner_html
from src.get_urls_recursively import *
from src.is_allowed_by_robots import *
from src import *

###### phase d'initialisation ######
# lecture du site Ensai.fr
url='https://ensai.fr'
url_base = get_url_base(url)
is_allowed = is_allowed_by_robots(url)
if is_allowed:
    # récupération de toutes les pages du site
    url_base_sitemap = url_base + "/sitemap_index.xml"
    all_urls_recursively = get_urls_recursively(url_base_sitemap)
    print(all_urls_recursively)

    # Initialisation 
    links_page_web = set()
    links_autorisés = set()
    links_interdits = set()

    ####### DEFINITIONS #####
    # page web : une url schema+nom de domaine
    # url = une url avec potentiellement tous les éléments possibles
    # href = une url (souvent issue de l'analyse d'un contenu html)
    # link = une url

    # pseudo code:
    # fonction récupérer_links_d'un_site(liste: liste des url d'un site): Return: liste: liste des links autorisées, liste
    # des links interdits et liste des 
    # pour chaque page on va récupérer les urls:
    # links_page_web = []
    # links_autorisés = []
    # links_interdits = []

    # pour chaque url dans all_url_recursively FAIRE
    #   hrefs = récupérer l'ensemble des href de l'url
    #   POUR CHAQUE href dans hrefs:
            # url_base = récupérer l'url de la page web de href (get_url_base() )
            # est_autorisé = vérifier si url_base est autorisée par son robot.txt
            # SI est_autorisé == TRUE ALORS
                # ajouter url_base à links_autorisés (links_autorisés.add(url_base))
                # ajouter href dans links_page_web
            # SINON ALORS
                # ajouter url_base à links_interdits
                
            
else:
    print(f"le site {url_base} ne permet pas qu'on le crawle")


