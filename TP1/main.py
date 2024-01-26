import importlib
import datetime
from sqlalchemy.exc import IntegrityError
from src.get_url_base import get_url_base
from src.is_allowed_by_robots import is_allowed_by_robots
from src.get_urls_recursively import get_urls_recursively
from src.classes.classes import Base, Page, Domaine, Frontiere
from src.create_session import create_session
from urllib.parse import urlparse



session = create_session()

# Pour vider toutes les tables au démarrage du programme
Base.metadata.drop_all(bind=engine)

try:
    # Phase d'initialisation
    url = 'https://ensai.fr'
    url_base = get_url_base(url)
    is_allowed = is_allowed_by_robots(url)

    domaine_1 = Domaine(url_base=url_base)
    session.add(domaine_1)
    session.commit()

except IntegrityError as e:
    print(f"Erreur d'intégrité : {e}")
    session.rollback()

except Exception as e:
    print(f"Une erreur s'est produite : {e}")
    session.rollback()

page_example = Page(url="http://example.com/page1", contenu_html="<html>...</html>", age=datetime.datetime.now())
page_example.domaine = domaine_1
session.add(page_example)
session.commit()
###### FIN phase d'initialisation ######################################################""


# demander une adresse à l'utilisateur
# url='https://ensai.fr'

while is_allowed_by_robots(url)==False:
    # demander à l'utilisateur une autre adresse
    url = input("Veuillez saisir une adresse URL : ")

# Vérifier la validité de l'URL
try:
    result = urlparse(url)
    if all([result.scheme, result.netloc]):
        print("L'adresse URL est valide.")
    else:
        print("L'adresse URL n'est pas valide.")
except ValueError:
    print("L'adresse URL n'est pas valide.")



##### INITIALISATION DES REFERENTIELS #####
set_sites_interdits = set()
set_frontière = set()
set_url_pages= set()
set_href=set()

# url_pages = [] # récupérer la liste des url des pages en base
# for url_page in url_pages:
    # set_url_pages.add(url)
    
# Constitution de la liste des sites interdits

# frontières_base = récupérer frontières en base
# for url in frontieres_base:
    # set_frontiere.add(url)


# SI mon url est interdite, alors je l'enlève de la frontière
# POUR CHAQUE url dans frontières_bases:
    # url_base = récupérer url du domaine
    # est_autorisé = True
    # SI url_base in site_interdits:
        # est_autorisé = False
    # est_autorisé = is_allowed_by_robots()
    # SI est_autorisé == False:
        # 
##### FIN INITIALISATION DES REFERENTIELS #####


# WAIT 3 secondes

# SI mon url est autorisée:
    # J'arrive sur une url
    # Je vérifie que mon url n'est pas dans url_pages
    # SI url not in url_pages:
        # je récupère la page et la charge en base
        # hrefs = je récupère les hrefs présents sur la page
        
        # --- Tri entre hrefs autorisés et interdits
        # POUR CHAQUE Href dans hrefs:
            # url_base = get_url_base(href)
            # SI url_base in site_interdits:

# SINON:
    # je vais

# N'oubliez pas de fermer la session après avoir terminé
session.close()








