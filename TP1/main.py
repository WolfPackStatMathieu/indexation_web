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

domaine_1 = Domaine(url_base=url_base)
session.add(domaine_1)
session.commit()


# # Exemple d'utilisation : création d'un objet Domaine avec un objet Robot associé
# domaine_example = Domaine(url_base="http://example.com", robot=robot_example)
# session.add(domaine_example)
# session.commit()

# # Exemple d'utilisation : création d'un objet Page associé à un objet Domaine

# page_example = Page(url="http://example.com/page1", contenu_html="<html>...</html>", age=datetime.datetime.now())
# page_example.domaine = domaine_example
# session.add(page_example)
# session.commit()


# N'oubliez pas de fermer la session après avoir terminé
session.close()








