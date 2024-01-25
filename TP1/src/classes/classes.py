from datetime import datetime

class Href:
    def __init__(self, url, est_autorise):
        self.url = url
        self.est_autorise = est_autorise
        self.pages = []  # Liste vide pour stocker les objets Page liés

class Page:
    def __init__(self, url, contenu_html, age):
        self.url = url
        self.contenu_html = contenu_html
        self.age = age
        self.domaine = None  # L'objet Domaine sera associé plus tard
        self.hrefs = []  # Liste vide pour stocker les objets Href liés

class Robot:
    def __init__(self, autorise):
        self.autorise = autorise

class Domaine:
    def __init__(self, url_base, robot):
        self.url_base = url_base
        self.pages = []  # Liste vide pour stocker les objets Page liés
        self.robot = robot  # robot doit être un objet de la classe Robot

    def ajouter_page(self, page):
        # Assigne le domaine à la page et ajoute la page à la liste
        page.domaine = self
        self.pages.append(page)

# # Exemple d'utilisation :
# # Création d'un objet Robot
# robot_example = Robot(autorise=True)

# # Création d'un objet Domaine
# domaine_example = Domaine(url_base="http://example.com", robot=robot_example)

# # Création d'un objet Page
# page_example = Page(url="http://example.com/page1", contenu_html="<html>...</html>", age=datetime.now())

# # Ajout de la page à la liste des pages du domaine
# domaine_example.ajouter_page(page_example)

# # Création d'un objet Href
# href_example = Href(url="http://example.com/link1", est_autorise=True)

# # Ajout de la page à la liste des pages liées à l'href
# href_example.pages.append(page_example)

# # Vous pouvez maintenant accéder aux pages, hrefs et domaines associés comme suit :
# # domaine_example.pages
# # page_example.hrefs
# # href_example.pages
