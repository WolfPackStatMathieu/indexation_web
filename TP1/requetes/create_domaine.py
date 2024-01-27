from sqlalchemy.exc import IntegrityError
from src.classes.classes import Domaine
from src.is_allowed_by_robots import is_allowed_by_robots
from src.get_url_base import get_url_base


def create_domaine(session, url):
    try:
        # Phase d'initialisation
        url_base = get_url_base(url)
        is_allowed = is_allowed_by_robots(url)

        domaine_1 = Domaine(url_base=url_base)
        session.add(domaine_1)
        session.commit()
        print(f'Le domaine {url_base} a été ajouté en base')
        return domaine_1
    except IntegrityError as e:
        print(f"Erreur d'intégrité : {e}")
        session.rollback()

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        session.rollback()
    
