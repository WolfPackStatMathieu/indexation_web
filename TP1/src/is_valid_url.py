from urllib.parse import urlparse

def is_valid_url(url):
    """dit si une url est valide ou non

    Args:
        url (string): url à vérifier

    Returns:
        boolean: True si c'est valide
    """
    try:
        result = urlparse(url)
        # Vérifie si les parties scheme et netloc sont présentes (URL valide)
        print(result.scheme)
        valid_scheme = result.scheme in ["http", "https"]
        print(result.netloc)
        valid_netloc = bool(result.netloc)
        # Exclut certaines URLs spécifiques, comme "/robots.txt"
        excluded_paths = ["/robots.txt", ""]
        excluded_url = result.path not in excluded_paths
        print(excluded_paths)

        return valid_scheme and valid_netloc and not excluded_url
    except ValueError:
        print(f"URL NON VALIDE: {url}")
        return False

if __name__ == "__main__":
    # Exemple d'utilisation
    url_to_check = "https://ensai.fr"
    if is_valid_url(url_to_check):
        print(f"L'URL {url_to_check} est valide.")
    else:
        print(f"L'URL {url_to_check} n'est pas valide.")