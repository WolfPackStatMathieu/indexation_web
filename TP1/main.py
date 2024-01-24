from bs4 import BeautifulSoup
import urllib.request
import urllib.robotparser

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

def can_fetch(url, user_agent='*'):
    """
    Vérifie si le crawler est autorisé à accéder à l'URL selon le robots.txt.
    """
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urllib.parse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp.can_fetch(user_agent, url)




########### Module robot #######
rp = urllib.robotparser.RobotFileParser()
url_robot = url_base + "/robots.txt"
rp.set_url(url_robot)
rp.read()

print(rp.can_fetch("*", url_base))