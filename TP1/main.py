import importlib
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.get_url_base import get_url_base
from src.is_allowed_by_robots import is_allowed_by_robots
from src.get_urls_recursively import get_urls_recursively
from src.classes.classes import Base, Href, Page, PageHrefAssociation, Robot, Domaine

# Chemin vers le fichier de base de données SQLite
db_path = "sqlite:///example.db"

# Création du moteur de la base de données
engine = create_engine(db_path, echo=True)

# Création des tables s'il n'existent pas encore
Base.metadata.create_all(bind=engine)

# Création d'une session pour interagir avec la base de données
Session = sessionmaker(bind=engine)
session = Session()



###### phase d'initialisation ######
# lecture du site Ensai.fr
url='https://ensai.fr'
url_base = get_url_base(url)
is_allowed = is_allowed_by_robots(url)

robot_example = Robot(autorise=is_allowed)
session.add(robot_example)
session.commit()

domaine_1 = Domaine(url_base=url_base, robot=robot_example)
session.add(domaine_1)
session.commit()


# récupération de toutes les pages du site
url_base_sitemap = url_base + "/sitemap_index.xml"
all_urls_recursively = get_urls_recursively(url_base_sitemap)
# print(all_urls_recursively)

# Initialisation 
links_page_web = set()
links_autorisés = set()
links_interdits = set()

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
            





# # Exemple d'utilisation : création d'un objet Robot et ajout à la base de données
# robot_example = Robot(autorise=True)
# session.add(robot_example)
# session.commit()

# # Exemple d'utilisation : création d'un objet Domaine avec un objet Robot associé
# domaine_example = Domaine(url_base="http://example.com", robot=robot_example)
# session.add(domaine_example)
# session.commit()

# # Exemple d'utilisation : création d'un objet Page associé à un objet Domaine

# page_example = Page(url="http://example.com/page1", contenu_html="<html>...</html>", age=datetime.datetime.now())
# page_example.domaine = domaine_example
# session.add(page_example)
# session.commit()

# # Exemple d'utilisation : création d'un objet Href et association avec un objet Page
# href_example = Href(url="http://example.com/link1", est_autorise=True)
# href_example.pages.append(page_example)
# session.add(href_example)
# session.commit()

# N'oubliez pas de fermer la session après avoir terminé
session.close()








