import importlib
import datetime
import time
import random
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
from src.fetch_url import fetch_url
from src.get_age import get_last_modified_date_of_url
from src.get_hrefs_from_url import get_hrefs_from_url

# Pour vider toutes les tables au démarrage du programme
session, engine = create_session()
Base.metadata.drop_all(bind=engine)
# on réétablit une session
session, engine = create_session()

# Appeler la fonction d'initialisation pour le domaine
domaine_1 = create_domaine(session, 'https://ensai.fr')

# # Utiliser la fonction pour ajouter une page
# url_page = 'http://example.com/page12'
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
max_nb_pages_stockees=10

pages_stockees = session.query(Page.url).all()
nombre_pages_stockees = len(pages_stockees)
# TANT QUE nombre_pages_stockees < max_nb_pages_stockees FAIRE:
while nombre_pages_stockees < max_nb_pages_stockees:
    # WAIT 3 secondes
    time.sleep(1)
    print(f'ON PARSE : {url}')
    pages_stockees = session.query(Page.url).all()
    # SI mon url est autorisée (robotparser gère le cas des erreurs 400 et disallow dans ce cas):
    est_autorise = is_allowed_by_robots(url)
    if est_autorise:
        # J'arrive sur une url
        # Vérifier combien de pages de ce domaines j'ai déjà
        url_base = get_url_base(url)
        # Initialiser le compteur nombre_pages_du_domaine à ce nombre.
        nombre_pages_du_domaine = compter_pages_d_un_domaine(url_base, session)
        print(nombre_pages_du_domaine)
        # SI le compteur < max_nb_pages_stockees ALORS:
        if nombre_pages_du_domaine < max_nb_pages_stockees:
            # Je vérifie que mon url n'est pas dans url_pages
            mon_url_est_deja_stockee = False
            if url in url_pages:
                mon_url_est_deja_stockee = True
            # SI url not in url_pages (sinon je passe à la suite) ALORS:
            if not mon_url_est_deja_stockee:
                # je récupère la page et la charge en base
                contenu_html = fetch_url(url)
                age_url = get_last_modified_date_of_url(url)
                # hrefs = je récupère les hrefs présents sur la page
                hrefs = get_hrefs_from_url(url)
                
                # on gère la création de Domaine
                result = None
                result = session.query(Domaine).filter_by(url_base=get_url_base(url)).first()
                if result is None:
                    domaine_1 = create_domaine(session, url)
                    
                domaine_id = session.query(Domaine).filter_by(url_base=get_url_base(url)).first()
                domaine_id = domaine_id.id
                url_page = url
                contenu_html_page = contenu_html
                age_url = get_last_modified_date_of_url(url)
                page_example = create_page(session, url_page, contenu_html_page, domaine_id, age = age_url)
                nombre_pages_stockees +=1
                # --- Tri entre hrefs autorisés et interdits
                # POUR CHAQUE Href dans hrefs:
                for href in hrefs:
                    url_base = get_url_base(href)
                    # SI url_base in site_interdits ALORS:
                    if url_base not in set_sites_interdits:
                        # je ne fais rien
                    # SINON:
                        # je vérifie que le site est autorisé
                        # est_autorise = is_allowed_by_robots(url)
                        # SI le site est autorisé ALORS:
                        if est_autorise:
                            # J'ajoute Href à set_frontiere: set_frontiere.add(Href)
                            set_frontiere.add(href)
                        # FIN SI
                    # FIN SI
                # FIN POUR
            # FIN SI
        # SINON:
            # Supprimer les url de Frontière et de set_frontiere
            set_frontiere.discard(url)
        # FIN SI

    # SINON:
        # Pour recommencer le processus je vais chercher une nouvelle url dans la frontiere
        # url = prends une url au hasard dans frontiere
    
    
    url = random.choice(list(set_frontiere)) # je prends une adresse au hasard dans la frontière 
    adresse_valide = False # j'initialise (peut être inutile ou mal placé)
    while adresse_valide == False:
        url_base = get_url_base(url) # je récupère l'adresse du domaine
        
        domaine = session.query(Domaine).filter_by(url_base=url).first() # je tente de récupérer le domaine s'il existe en base
        if domaine is not None:
            domaine_id = domaine.id # je chope l'id 
            # je récupère les Pages liées à ce domaine
            pages_stockees_url_base = session.query(Page.url).filter_by(domaine_id=domaine_id).all()
            # si j'ai plus de 5 pages ALORS:
            if len(pages_stockees_url_base) >= 5:
                set_frontiere.discard(url) # je supprime l'url choisie au hasard de ma frontière pour ne pas retomber dessus
                url = random.choice(list(set_frontiere)) # j'en prends une autre
                adresse_valide = True # je quitte ma boucle
        # Si le domaine est None, c'est que je n'ai pas de page de ce domaine
        adresse_valide = True # je quitte ma boucle    
            
    
    print(f'nombre de pages stockées: {nombre_pages_stockees}')
# N'oubliez pas de fermer la session après avoir terminé

# Récupération des domaines depuis la base de données
pages = session.query(Page.url).all()

# Écriture des domaines dans le fichier crawled_webpages.txt
with open('crawled_webpages.txt', 'w') as fichier:
    for page in pages:
        fichier.write(f"{page.url}\n")
        
        
session.close()








