import importlib
import datetime
from sqlalchemy.exc import IntegrityError
from src.get_url_base import get_url_base
from src.is_allowed_by_robots import is_allowed_by_robots
from src.get_urls_recursively import get_urls_recursively
from src.classes.classes import Base, Page, Domaine, Frontiere
from src.create_session import create_session
from urllib.parse import urlparse
from requetes.create_domaine import create_domaine
from requetes.create_page import create_page


# Pour vider toutes les tables au démarrage du programme
session, engine = create_session()
Base.metadata.drop_all(bind=engine)
# on réétablit une session
session, engine = create_session()

# Appeler la fonction d'initialisation pour le domaine
# domaine_1 = create_domaine(session, 'https://ensai.fr')

# Utiliser la fonction pour ajouter une page
# url_page = 'http://example.com/page1'
# contenu_html_page = "<html>...</html>"
# page_example = create_page(session, url_page, contenu_html_page, domaine_1)

###### FIN phase d'initialisation ######################################################""


# demander une adresse à l'utilisateur
url='https://ensai.fr'
# url = input("Veuillez saisir une adresse URL : ")
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
set_domaines=set()

# url_pages = [] # récupérer la liste des url des pages en base
url_pages = session.query(Page.url).all()
for url_page in url_pages:
    set_url_pages.add(url)
nombre_pages_stockées = len(set_url_pages) 

print(f'Il y a {nombre_pages_stockées} pages en base pour le domaine {url}')
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


# TANT QUE nombre_pages_stockées < max_nb_pages_stockées FAIRE:
    # WAIT 3 secondes

    # SI mon url est autorisée (robotparser gère le cas des erreurs 400 et disallow dans ce cas):
        # J'arrive sur une url
        # Vérifier combien de pages de ce domaines j'ai déjà
        # Initialiser le compteur nombre_pages_du_domaine à ce nombre.
        # SI le compteur < max_pages_par_domaine ALORS:
            # Je vérifie que mon url n'est pas dans url_pages
            # SI url not in url_pages (sinon je passe à la suite) ALORS:
                # je récupère la page et la charge en base
                
                # hrefs = je récupère les hrefs présents sur la page
                
                # --- Tri entre hrefs autorisés et interdits
                # POUR CHAQUE Href dans hrefs:
                    # url_base = get_url_base(href)
                    # SI url_base in site_interdits ALORS:
                        # je ne fais rien
                    # SINON:
                        # je vérifie que le site est autorisé
                        # SI le site est autorisé ALORS:
                            # J'ajoute Href à set_frontiere: set_frontiere.add(Href)
                        # FIN SI
                    # FIN SI
                # FIN POUR
            # FIN SI
        # SINON:
            # Supprimer les url de Frontière et de set_frontiere
        # FIN SI

    # SINON:
        # Pour recommencer le processus je vais chercher une nouvelle url dans la frontiere
        # url = prends une url au hasard dans frontiere
        

# N'oubliez pas de fermer la session après avoir terminé
session.close()








