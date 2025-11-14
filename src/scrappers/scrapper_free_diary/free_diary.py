from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import page_free_diary as pfd
from bs4 import BeautifulSoup

URL = "https://www.diariolibre.com/ultima-hora"
scrapper = pfd.PageFreeDiary()

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
        count = 1

        for art in articles:
            title = art.select_one("h2 a")
            img = art.select_one("img")
            link = None
            if title and title.has_attr("href"):
                link = "https://www.diariolibre.com" + title["href"]
            else:
                print("No se encontró enlace en noticia")
                link = "https://www.diariolibre.com"

            self.news.append({
                "source_information": "Diario Libre",
                'title': title.get_text(strip=True) if title else None,
                'link': link,
                'summary': scrapper.page_free_diary(
                    "https://www.diariolibre.com" + title["href"]
                    ),
                'url_link': img["src"] if img else None
            })
            if count == 1:
                break
            count += 1

        driver.quit()
        return self.news
