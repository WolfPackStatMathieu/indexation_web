from sqlalchemy.exc import IntegrityError
from src.classes.classes import Page
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

def create_page(session, url, contenu_html, domaine_id, age):
    try:
        # Phase d'initialisation
        page_example = Page(url=url, contenu_html=contenu_html, age=age, domaine_id=domaine_id)
        session.add(page_example)
        session.commit()
        print(f"La page {url} a été ajoutée en base pour le domaine {domaine_id}")
        return page_example

    except IntegrityError as e:
        print(f"Erreur d'intégrité : {e}")
        session.rollback()

    except (NoResultFound, MultipleResultsFound) as e:
        print(f"Aucun ou plusieurs domaines correspondants à l'URL de la page : {e}")
        session.rollback()

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        session.rollback()
