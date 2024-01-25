"""Fonction pour récupérer le contenu d'une URL"""
import requests

def fetch_url(url):
    """retourne le contenu html d'une url

    Args:
        url (string): une page web à visiter

    Returns:
        string: le contenu html
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

if __name__=='__main__':
    import requests
    html_content = fetch_url("http://www.ensai.fr")
    print(html_content)