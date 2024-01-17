import requests
from bs4 import BeautifulSoup


def get_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, "xml")
    urls = [element.text for element in soup.find_all("loc")]
    return urls


def save_to_file(urls, filename):
    with open(filename, 'w') as f:
        for url in urls:
            f.write(url + "\n")


# replace with your sitemap url
sitemap_url = "https://carregados.com.br/sitemap.xml"
urls = get_sitemap_urls(sitemap_url)
save_to_file(urls, "urls.txt")
