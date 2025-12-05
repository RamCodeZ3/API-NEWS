from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrappers.scrapper_free_diary.page_free_diary import PageFreeDiary 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

URL = "https://www.diariolibre.com/ultima-hora"
scrapper = PageFreeDiary()

class FreeDiary():
    def __init__(self):
        self.news = []

    def news_free_diary(self, count:int):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        service = Service(log_path='NUL')
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(URL)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        articles = soup.select("article")
        count2 = 1

        for art in articles:
            title = art.select_one("h2 a")
            category = art.select_one("div a.event")
            link = None
            if title and title.has_attr("href"):
                link = "https://www.diariolibre.com" + title["href"]
            else:
                print("No se encontró enlace en noticia")
                link = "https://www.diariolibre.com"

            self.news.append({
                "source_information": "Diario Libre",
                "category": category.get_text(strip=True),
                'title': title.get_text(strip=True) if title else None,
                'link': link,
                'summary': scrapper.page_free_diary(
                    "https://www.diariolibre.com" + title["href"]
                    ),
            })
            if count2 == count:
                break
            count2 += 1

        driver.quit()
        return self.news
