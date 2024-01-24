from bs4 import BeautifulSoup
import urllib.request
from src import retourner_html
from src.get_urls_recursively import *

###### phase d'initialisation ######
# lecture du site Ensai.fr
url_base ='https://ensai.fr'
# récupération de toutes les pages du site
all_urls_recursively = get_urls_recursively(url_base)
print(all_urls_recursively)
# pour chaque page on va récupérer les urls



