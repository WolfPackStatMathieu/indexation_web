from bs4 import BeautifulSoup
import urllib.request


url_base ='http://ensai.fr'
with urllib.request.urlopen(url_base) as f:
    html_doc = f.read().decode('utf-8')

soup = BeautifulSoup(html_doc, 'html.parser')


mes_href = []
for link in soup.find_all('a'):
    mes_href.append(link.get('href'))
    # print(link.get('href'))

print(len(mes_href))


liste_url_final=[]
liste_url_final.append(mes_href[:5])


# si c'est True, alors on lance Beautifulsoup et 
# on récupère les href

