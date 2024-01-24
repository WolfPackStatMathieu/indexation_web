import requests
from bs4 import BeautifulSoup


import requests
from bs4 import BeautifulSoup
from http.client import IncompleteRead

def get_all_entries_from_xml(url, max_retries=3):
    """retourne toutes les urls d'un site à partir de sa page /site_map_index.xml

    Args:
        url (string): monsite/site_map_index.xml

    Returns:
        list: liste de toutes les urls d'un même site web
    """
    for retry in range(max_retries):
        try:
            with requests.get(url) as r:
                r.raise_for_status()
                soup = BeautifulSoup(r.text, "xml")

                all_url_tags = soup.find_all("url")
                allUrls = [urls.findNext("loc").text for urls in all_url_tags]

                sitemapList = soup.find_all("sitemap")
                allSitemaps = [sitemap.findNext("loc").text for sitemap in sitemapList]

                return {"sitemaps": allSitemaps, "urls": allUrls}

        except IncompleteRead as e:
            print(f"Error during request to {url}: {e}")
            print(f"Retrying ({retry + 1}/{max_retries})...")
            continue

        except requests.exceptions.RequestException as e:
            print(f"Error during request to {url}: {e}")
            return {"sitemaps": [], "urls": []}

    print(f"Max retries reached for {url}")
    return {"sitemaps": [], "urls": []}


def get_urls_recursively(url) :
    xml = get_all_entries_from_xml(url)
    allUrls = xml['urls']
    sitemaps = xml['sitemaps']
    visitedSitemaps = []

    while (sitemaps) :
        for sitemap in sitemaps :
            if sitemap not in visitedSitemaps :
                visitedSitemaps.append(sitemap)
                xml = get_all_entries_from_xml(sitemap)
                sitemaps.extend(xml['sitemaps'])

                for elt in xml['urls'] :
                    allUrls.append(elt)
            else :
                sitemaps.remove(sitemap)

    return(allUrls)

if __name__=='__main__':
    # Scraper récursivement toutes les URLs à partir d'un sitemap ou index de sitemap
    all_urls_recursively = get_urls_recursively("https://ensai.fr/sitemap_index.xml")

    with open("urls.txt","w+") as f :
        for url in all_urls_recursively :
            f.write(url+"\n")
            
    for url in all_urls_recursively : 
        print(url)
    print(type(all_urls_recursively))
    
    