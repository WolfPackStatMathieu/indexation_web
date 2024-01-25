"""cette fonction sert à mapper un domaine, avec toutes ses pages
et où chaque page a un ensemble de Href autorisés ou non
"""
import sys
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
print(sys.path)

from get_urls_recursively import get_urls_recursively
from get_url_base import get_url_base
from fetch_url import fetch_url
from classes.classes import Base, Domaine, Page

def create_session():
    db_path = "sqlite:///example.db"
    engine = create_engine(db_path, echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()


def mapper_un_domaine(url_domaine, session):
    
        
    url_base = get_url_base(url_domaine)
    # récupération de toutes les pages du site
    url_base_sitemap = url_base + "/sitemap_index.xml"
    all_urls_recursively = get_urls_recursively(url_base_sitemap)
    # print(all_urls_recursively)

    # Initialisation 
    links_page_web = set() # on stocke les pages du domaine en cours
    links_autorisés = set() # on stocke les liens dont le domaine est autorisé
    links_interdits = set() # on stocke les liens dont le domaine est interdit

    # pseudo code:
    # fonction récupérer_links_d'un_site(liste: liste des url d'un site): Return: liste: liste des links autorisées, liste
    # des links interdits et liste des 
    # pour chaque page on va récupérer les urls:
    for page in all_urls_recursively:
        contenu_html_page = fetch_url(page) 
        
        # trouver l'id du domaine correspondant url_base
        domaine = session.query(Domaine).filter_by(url_base=url_base).first()
        
        if domaine:
            # Si le domaine existe, on peut créer l'objet Page associé
            # TODO ajouter fonction age
            ma_page = Page(url=page, contenu_html=contenu_html_page, age=datetime.datetime.now())
            ma_page.domaine = domaine

            session.add(ma_page)
            session.commit()
        
        # hrefs = get_hrefs_from_url(page)
        # for href in hrefs:
        #     url_base = get_url_base(href)
        #     est_autorise = est_autorise(url_base)
        #     if est_autorise:
        #         href_example = Href(url=href, est_autorise=True)
        #         href_example.pages.append(page)
        #         # session.add(href_example)
        #         # session.commit()


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
                


    pass

if __name__ == '__main__':
    # Créer la session une fois avant d'appeler la fonction
    session = create_session()
    import sys
    from get_urls_recursively import get_urls_recursively
    from get_url_base import get_url_base
    domaine = 'https://ensai.fr'
    mapper_un_domaine(url_domaine=domaine, session=session)
    
    session.close()