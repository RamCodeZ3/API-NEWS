import requests
from bs4 import BeautifulSoup


class PageTheNewDiary:
    def __init__(self):
        self.summary = ""

    def page_the_new_diary(self, url):
        response = requests.get(url, timeout=10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")

        container = soup.select_one("div.entry-content.mt-md-4.mt-3")
        if not container:
            return None

        paragraphs = container.find_all("p") if container else []

        self.summary = " ".join(
            p.get_text(" ", strip=True) 
            for p in paragraphs
        )

        return self.summary
