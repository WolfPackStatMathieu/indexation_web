"""cette fonction sert à mapper un domaine, avec toutes ses pages
et où chaque page a un ensemble de Href autorisés ou non
"""
import sys
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from get_urls_recursively import get_urls_recursively
from get_url_base import get_url_base
from fetch_url import fetch_url
from classes.classes import Base, Domaine, Page, Frontiere
from create_session import create_session
from get_url_sitemap_index import get_url_sitemap_index
from get_pages_for_domain import get_pages_for_domain


def mapper_un_domaine(domaine, session):
    """prend un domaine et retourne ses url et date de modifications
    Args:
        domaine (Domaine): le Domaine à mapper
        session (session): la session en cours pour la base de donnée
    """
    
    url_domaine = domaine.url_base
    url_base = get_url_base(url_domaine)
    # récupération de toutes les url du site (avec leur date de last modification)
    url_base_sitemap = get_url_sitemap_index(url_base)
    all_urls_recursively = get_urls_recursively(url_base_sitemap)

    return all_urls_recursively

if __name__ == '__main__':
    # Créer la session une fois avant d'appeler la fonction
    session = create_session()
    import sys
    from get_urls_recursively import get_urls_recursively
    from get_url_base import get_url_base
    
    url_domaine = 'https://ensai.fr'
    print(url_domaine)
    domaine  = session.query(Domaine).filter_by(url_base=url_domaine).first()

    print(mapper_un_domaine(domaine=domaine, session=session))
    
    session.close()