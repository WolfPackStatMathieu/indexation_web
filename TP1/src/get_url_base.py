"""Cette fonction prend en entrée un lien url et retourne l'url de base avec le scheme et 
retourne une string constituée du protocole et du nom de domaine.
"""
from urllib.parse import urlparse, urlunparse

def get_url_base(url):
    """retourne à partir d'une url une string constituée du protocole et le nom de domaine

    Args:
        url (string): une url plus ou moins longue

    Returns:
        string: protocole + nom de domaine
    """
    # Extrait la partie de base de l'URL (sans le chemin spécifique)
    parsed_url = urlparse(url)
    url_base = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
    
    return url_base

if __name__ == '__main__':
    from urllib.parse import urlparse, urlunparse
    mon_url = 'https://www.google.com/search?client=ubuntu-sn&hs=e7I&sca_esv=601333276&channel=fs&sxsrf=ACQVn08mcrS3-Wxpc4KwrYZiAY9740BWjQ:1706167319592&q=structure+d%27un+lien+url&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjhzYvIgPiDAxWbcKQEHcJVAQIQ0pQJegQICBAB&biw=2066&bih=1049&dpr=0.9'
    mon_url_base = get_url_base(mon_url)
    print(mon_url_base)