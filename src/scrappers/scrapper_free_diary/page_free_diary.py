from bs4 import BeautifulSoup
import requests


class PageFreeDiary:
    def __init__(self):
        self.summary = ""

    def page_free_diary(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        article = soup.find("div", class_="detail-body")
        if article is None:
            print("No se encontró el artículo en:", url)
            return "Artículo no disponible"
        
        paragraphs = article.find_all("p")

        self.summary = " ".join(p.get_text(
            " ",
            strip=True) for p in paragraphs)
        
        return self.summary
