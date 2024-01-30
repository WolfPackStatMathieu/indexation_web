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
        valid_scheme = result.scheme in ["http", "https"]
        valid_netloc = bool(result.netloc)
        # Exclut certaines URLs spécifiques, comme "/robots.txt"
        excluded_paths = ["/robots.txt"]
        excluded_url = result.path in excluded_paths

        return valid_scheme and valid_netloc and not excluded_url
    except ValueError:
        return False