from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from news.news_pages.page_free_diary import PageFreeDiary
from bs4 import BeautifulSoup
import time

URL = "https://www.diariolibre.com/ultima-hora"
scrapper = PageFreeDiary()

class FreeDiary:
    def __init__(self):
        self.news = []

    def news_free_diary(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(URL)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        articles = soup.select("article")

        for art in articles:
            title = art.select_one("h2 a")
            img = art.select_one("img")

            self.news.append({
                "source_information": "Diario Libre",
                'title': title.get_text(strip=True) if title else None,
                'link': "https://www.diariolibre.com" + title["href"] if title else None,
                'summary': scrapper.page_free_diary(
                    "https://www.diariolibre.com" + title["href"]
                    ),
                'url_link': img["src"] if img else None
            })

        driver.quit()
        return self.news
