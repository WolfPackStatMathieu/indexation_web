"""cette fonction sert à mapper un domaine, avec toutes ses pages
et où chaque page a un ensemble de Href autorisés ou non
"""
import sys
sys.path.append("..")
from src.get_urls_recursively import get_urls_recursively
from src.get_url_base import get_url_base

def mapper_un_domaine(url_domaine):
    
        
    url_base = get_url_base(url_domaine)
    # récupération de toutes les pages du site
    url_base_sitemap = url_base + "/sitemap_index.xml"
    all_urls_recursively = get_urls_recursively(url_base_sitemap)
    # print(all_urls_recursively)

    # Initialisation 
    links_page_web = set() # on stocke les pages du domaine en cours
    links_autorisés = set() # on stocke les liens dont le domaine est autorisé
    links_interdits = set() # on stocke les liens dont le domaine est interdit

    for page in all_urls_recursively
    # pseudo code:
    # fonction récupérer_links_d'un_site(liste: liste des url d'un site): Return: liste: liste des links autorisées, liste
    # des links interdits et liste des 
    # pour chaque page on va récupérer les urls:


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
    import sys
    sys.path.append("..")
    from src.get_urls_recursively import get_urls_recursively
    from src.get_url_base import get_url_base
    domaine = 'https://ensai.fr'
    mapper_un_domaine(domaine)