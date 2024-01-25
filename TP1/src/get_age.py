import requests
from bs4 import BeautifulSoup
from http.client import IncompleteRead

def get_all_entries_from_xml(url, max_retries=3):
    """Retourne toutes les URLs d'un site et les dates de dernière modification à partir de sa page /site_map_index.xml.

    Args:
        url (string): URL du sitemap, typiquement monsite.com/sitemap.xml

    Returns:
        dict: Dictionnaire avec les clés 'sitemaps' et 'urls', contenant respectivement les URLs des sitemaps et des pages avec leur date de dernière modification.
    """
    for retry in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "xml")

            all_url_tags = soup.find_all("url")
            allUrls = [(url_tag.find("loc").text, url_tag.find("lastmod").text if url_tag.find("lastmod") else "Non disponible") for url_tag in all_url_tags]

            sitemapList = soup.find_all("sitemap")
            allSitemaps = [(sitemap_tag.find("loc").text, sitemap_tag.find("lastmod").text if sitemap_tag.find("lastmod") else "Non disponible") for sitemap_tag in sitemapList]

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

# # Test the function
# sitemap_url = "https://www.ensai.fr/sitemap_index.xml"  # Replace with the actual sitemap URL
# sitemap_data = get_urls_recursively(sitemap_url)
# print(sitemap_data)

def get_urls_recursively(url):
    xml = get_all_entries_from_xml(url)
    allUrlsWithDates = xml['urls']  # Liste des tuples (URL, date de dernière modification)
    sitemaps = xml['sitemaps']
    visitedSitemaps = []

    while sitemaps:
        newSitemaps = []  # Pour stocker les nouveaux sitemaps trouvés dans cette itération
        for sitemap, _ in sitemaps:
            if sitemap not in visitedSitemaps:
                visitedSitemaps.append(sitemap)
                xml = get_all_entries_from_xml(sitemap)
                newSitemaps.extend(xml['sitemaps'])

                for url, lastmod in xml['urls']:
                    allUrlsWithDates.append((url, lastmod))
        sitemaps = newSitemaps  # Mettre à jour la liste des sitemaps à visiter

    return allUrlsWithDates

# if __name__ == '__main__':
#     # Scraper récursivement toutes les URLs à partir d'un sitemap ou index de sitemap
#     all_urls_recursively = get_urls_recursively("https://ensai.fr/sitemap_index.xml")

#     with open("urls.txt", "w+") as f:
#         for url, lastmod in all_urls_recursively:
#             f.write(f"{url}, Last Modified: {lastmod}\n")
            
#     for url, lastmod in all_urls_recursively:
#         print(f"{url}, Last Modified: {lastmod}")
#     print(type(all_urls_recursively))


def get_last_modified_date_of_url(sitemap_url, base_url):
    all_urls_with_dates = get_urls_recursively(sitemap_url)
    
    for url, last_modified in all_urls_with_dates:
        if url == base_url:
            return last_modified
    
    return "Date de dernière modification non trouvée pour l'URL spécifiée."


if __name__ == '__main__':
    base_url = "https://ensai.fr/"
    sitemap_url = base_url + "sitemap_index.xml"

    last_modified_date = get_last_modified_date_of_url(sitemap_url, base_url)
    print(f"Date de dernière modification pour {base_url} : {last_modified_date}")


