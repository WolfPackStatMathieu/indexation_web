import requests
import urllib

def retourner_html(url_base):
    """retourne le code html de l'url fournie

    Args:
        url_base (string): url de la source

    Returns:
        string: code html de la page web 
    """
    with urllib.request.urlopen(url_base) as f:
        html_doc = f.read().decode('utf-8')
    return html_doc

if __name__ == '__main__':
    import requests
    import urllib
    html_ensai = retourner_html("https://ensai.fr/")
    print(html_ensai)