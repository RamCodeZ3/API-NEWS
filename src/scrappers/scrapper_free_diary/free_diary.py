from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrappers.scrapper_free_diary.page_free_diary import PageFreeDiary 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from datetime import datetime


URL = "https://www.diariolibre.com/ultima-hora"
scrapper = PageFreeDiary()


class FreeDiary():
    def __init__(self):
        self.news = []

    async def news_free_diary(self, count:int):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--remote-debugging-port=0")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-webgl")
        options.add_argument("--disable-webgl2")
        
        service = Service(log_path='NUL')
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(URL)

        try:
            soup = BeautifulSoup(driver.page_source, "html.parser")
            articles = soup.select("article")
            count2 = 1

            for art in articles:
                title = art.select_one("h2 a")
                category = art.select_one("div a.event")

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
                    "scrapper_at": datetime.utcnow().isoformat()
                })
                if count2 == count:
                    break
                count2 += 1

            driver.quit()
            print("✅ Se realizo el webscraping del Diario Libre con exito")
            return self.news
        
        except:
           print("❌ No se pudo completar el webscraping de Diario Libre.")
