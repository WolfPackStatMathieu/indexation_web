import importlib
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.get_url_base import get_url_base
from src.is_allowed_by_robots import is_allowed_by_robots
from src.get_urls_recursively import get_urls_recursively
from src.classes.classes import Base, Page, Domaine, Frontiere
from src.create_session import create_session

session = create_session()

###### phase d'initialisation ######
# lecture du site Ensai.fr
url='https://ensai.fr'
url_base = get_url_base(url)
is_allowed = is_allowed_by_robots(url)

domaine_1 = Domaine(url_base=url_base)
session.add(domaine_1)
session.commit()

page_example = Page(url="http://example.com/page1", contenu_html="<html>...</html>", age=datetime.datetime.now())
page_example.domaine = domaine_1
session.add(page_example)
session.commit()




# N'oubliez pas de fermer la session après avoir terminé
session.close()








