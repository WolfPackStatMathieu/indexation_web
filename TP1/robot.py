import urllib.robotparser


def robots_entre(url_base):
    """permet de savoir si le robot est autorisé à parser l'url

    Args:
        url_base (string): l'url du site que l'on veut parser

    Returns:
        boolean: True si le robot a le droit d'entrer, False sinon
    """
    rp = urllib.robotparser.RobotFileParser()
    url_robot = url_base + "/robots.txt"
    rp.set_url(url_robot)
    rp.read()

    return rp.can_fetch("*", url_base)