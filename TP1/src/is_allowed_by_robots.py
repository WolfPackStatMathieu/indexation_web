"""Fonction pour vérifier l'autorisation dans le fichier robots.txt pour une URL de base
"""
import urllib.robotparser
from get_url_base import *
def is_allowed_by_robots(url):
    """permet de savoir si un site web autorise un robot à le crawler

    Args:
        url (string): une page d'un site web

    Returns:
        bolean: True si le robot est autorisé, False sinon
    """
    base_url = get_url_base(url)
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(base_url + "/robots.txt")
    rp.read()
    print(f'le site {base_url} est autorisé: {rp.can_fetch("*", url)}')
    return rp.can_fetch("*", url)

if __name__ == '__main__':
    import urllib.robotparser
    seed_url_1 = "https://www.google.com/search?client=ubuntu-sn&hs=e7I&sca_esv=601333276&channel=fs&sxsrf=ACQVn08mcrS3-Wxpc4KwrYZiAY9740BWjQ:1706167319592&q=structure+d'un+lien+url&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjhzYvIgPiDAxWbcKQEHcJVAQIQ0pQJegQICBAB&biw=2066&bih=1049&dpr=0.9"
    
    is_allowed_by_robots(seed_url_1)
    seed_url_2 = "https://ensai.fr/3-vie-etudiante/les-associations/"
    is_allowed_by_robots(seed_url_2)