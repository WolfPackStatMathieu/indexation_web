import requests
from bs4 import BeautifulSoup


def get_all_entries_from_xml(url) :
    """retourne toutes les urls d'un site à partir de sa page /site_map_index.xml

    Args:
        url (string): monsite/site_map_index.xml

    Returns:
        list: liste de toutes les urls d'un même site web
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "xml")

    # URLS
    all_url_tags = soup.find_all("url")
    allUrls = []
    for urls in all_url_tags :
        allUrls.append(urls.findNext("loc").text)

    # SITEMAPS
    sitemapList = soup.find_all("sitemap")
    allSitemaps = []
    for sitemap in sitemapList:
        allSitemaps.append(sitemap.findNext("loc").text)

    return ({"sitemaps" : allSitemaps, "urls" : allUrls})

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
    
    