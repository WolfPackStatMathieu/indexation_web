"""Cette fonction compter_pages_d_un_domaine prend l'URL
du domaine et la session SQLAlchemy en argument. Elle 
recherche d'abord le domaine correspondant à l'URL donnée,
puis récupère toutes les pages associées à ce domaine. Enfin,
elle compte le nombre de pages et le retourne. Vous pouvez 
appeler cette fonction avec l'URL de votre domaine et la
session appropriée.

    Returns:
        int: nombre de pages du domaine
    """

from sqlalchemy.orm import joinedload
from src.classes.classes import Domaine, Page

def compter_pages_d_un_domaine(url_domaine, session):
    # Rechercher le domaine correspondant à l'url_domaine
    domaine = session.query(Domaine).filter_by(url_base=url_domaine).first()

    if domaine:
        # Si le domaine existe, récupérer toutes les pages associées à ce domaine
        pages_du_domaine = session.query(Page).filter_by(domaine=domaine).all()

        # Compter le nombre de pages
        nombre_de_pages = len(pages_du_domaine)

        # Vous pouvez maintenant utiliser la variable `nombre_de_pages` comme nécessaire
        print(f"Le nombre de pages pour le domaine {url_domaine} est : {nombre_de_pages}")

        # Retourner le nombre de pages
        return nombre_de_pages

    else:
        print(f"Aucun domaine trouvé pour l'URL : {url_domaine}")
        return 0  # Retourner 0 s'il n'y a pas de domaine correspondant à l'url_domaine


if __name__ == '__main__':
    from create_session import create_session
    from classes.classes import Domaine, Page
    import datetime
    from sqlalchemy.orm import declarative_base
    from sqlalchemy import create_engine
    
    # Création de la base de données et de la structure
    engine = create_engine('sqlite:///example.db', echo=True)
    Base = declarative_base()
    Base.metadata.create_all(bind=engine)
    
    
    session = create_session()
    url='https://ensai.fr'
    
    # Créer un objet Domaine
    domaine_1 = Domaine(url_base=url)
    session.add(domaine_1)
    session.commit()
    
    nombre_page_ensai = compter_pages_d_un_domaine(url_domaine=url, session=session)
    
    # Créer deux objets Page reliés à domaine_1
    page_1 = Page(url='https://ensai.fr/page1', contenu_html='<html>Contenu de la page 1</html>', age=datetime.datetime.now(), domaine=domaine_1)
    
    
    page_2 = Page(url='https://ensai.fr/page2', contenu_html='<html>Contenu de la page 2</html>', age=datetime.datetime.now(), domaine=domaine_1)

    # Ajouter les pages à la session et effectuer la transaction
    session.add_all([page_1, page_2])
    session.commit()
    
    # Récupérer à nouveau le domaine après l'ajout des pages
    domaine_1 = session.query(Domaine).filter_by(url_base=url).first()
    
    print(domaine_1.pages)
    # Compter les pages du domaine après l'ajout
    nombre_page_ensai = compter_pages_d_un_domaine(url_domaine=url, session=session)
    print(f"Nombre total de pages pour {url} après ajout : {nombre_page_ensai}")

    