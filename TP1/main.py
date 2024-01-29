import importlib
import datetime
import time
from sqlalchemy.exc import IntegrityError
from src.get_url_base import get_url_base
from src.is_allowed_by_robots import is_allowed_by_robots
from src.get_urls_recursively import get_urls_recursively
from src.classes.classes import Base, Page, Domaine, Frontiere
from src.create_session import create_session
from urllib.parse import urlparse
from requetes.create_domaine import create_domaine
from requetes.create_page import create_page
from src.compter_pages_d_un_domaine import compter_pages_d_un_domaine

# Pour vider toutes les tables au démarrage du programme
session, engine = create_session()
Base.metadata.drop_all(bind=engine)
# on réétablit une session
session, engine = create_session()

# Appeler la fonction d'initialisation pour le domaine
domaine_1 = create_domaine(session, 'https://ensai.fr')

# Utiliser la fonction pour ajouter une page
url_page = 'http://example.com/page12'
contenu_html_page = "<html>...</html>"
page_example = create_page(session, url_page, contenu_html_page, domaine_1)

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
set_frontiere = set()
set_url_pages= set()
set_domaines=set()

# url_pages = [] # récupérer la liste des url des pages en base
url_pages = session.query(Page.url).all()
for url_page in url_pages:
    set_url_pages.add(url)
nombre_pages_stockees = len(set_url_pages) 

print(f'Il y a {nombre_pages_stockees} pages en base pour le domaine {url}')
# Constitution de la liste des sites interdits

frontieres_base = session.query(Frontiere.url).all()

for url in frontieres_base:
    set_frontiere.add(url)

# SI une url est interdite, alors je l'enlève de la frontière
# POUR CHAQUE url dans frontières_bases:
for url in frontieres_base:
    # url_base = récupérer url du domaine
    url_base = get_url_base(url)
    est_autorise = True
    # SI url_base in site_interdits:
    if url_base in set_sites_interdits:
        est_autorise = False
        set_frontiere.remove(url)
        
    est_autorise = is_allowed_by_robots()
    # SI est_autorisé == False:
    if est_autorise == False:
        set_frontiere.remove(url)

##### FIN INITIALISATION DES REFERENTIELS #####
max_nb_pages_stockees=5

pages_stockees = session.query(Page.url).all()
nombre_pages_stockees = len(pages_stockees)
# TANT QUE nombre_pages_stockees < max_nb_pages_stockees FAIRE:
while nombre_pages_stockees < max_nb_pages_stockees:
    # WAIT 3 secondes
    time.sleep(1)
    # SI mon url est autorisée (robotparser gère le cas des erreurs 400 et disallow dans ce cas):
    if is_allowed_by_robots(url):
        # J'arrive sur une url
        # Vérifier combien de pages de ce domaines j'ai déjà
        url_base = get_url_base(url)
        # Initialiser le compteur nombre_pages_du_domaine à ce nombre.
        nombre_pages_du_domaine = compter_pages_d_un_domaine(url_base, session)
        print(nombre_pages_du_domaine)
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
        
    nombre_pages_stockees +=1
    print(f'nombre de pages stockées: {nombre_pages_stockees}')
# N'oubliez pas de fermer la session après avoir terminé
session.close()








