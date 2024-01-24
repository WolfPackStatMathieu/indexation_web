from abc import ABC, abstractmethod

# Composant de base
class UrlComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Feuille (représente un lien URL individuel)
class UrlLeaf(UrlComponent):
    def __init__(self, url):
        self.url = url

    def display(self):
        print(f"URL: {self.url}")

# Composite (représente une page avec des liens URL)
class UrlComposite(UrlComponent):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f"Page Title: {self.title}")
        for child in self.children:
            child.display()

# Exemple d'utilisation
if __name__ == "__main__":
    # Création de la structure
    page = UrlComposite("www.ensai.fr")
    page.add(UrlLeaf("www.ensai.fr/page1"))
    page.add(UrlLeaf("www.ensai.fr/page2"))

    subpage = UrlComposite("www.ensai.fr/subpage")
    subpage.add(UrlLeaf("www.ensai.fr/subpage/page3"))
    subpage.add(UrlLeaf("www.ensai.fr/subpage/page4"))

    page.add(subpage)

    # Affichage de la structure
    page.display()
