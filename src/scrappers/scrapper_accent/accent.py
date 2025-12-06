from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from scrappers.scrapper_accent.page_accent import PageAccent
from datetime import datetime


URL = "https://acento.com.do/seccion/actualidad.html"
scrapper = PageAccent()


class Accent:
    def __init__(self):
        self.news = []

    async def news_accent(self, count: int):
        options = Options()
        options.add_argument("--headless")
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
        
        try:
            driver = webdriver.Chrome(options=options, service=service)
            driver.set_page_load_timeout(60)
            driver.implicitly_wait(10)
            driver.get(URL)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            articles = soup.select("article.entry-box.entry-box--standard")
            count2 = 1

            for art in articles:
                title = art.select_one("a.cover-link")
                category = art.select_one("div.entry-data-upper-container p")

                self.news.append({
                    "source_information": "acento",
                    "category": category.get_text(strip=True),
                    'title': title["title"] if title else None,
                    'link': title["href"],
                    'summary': scrapper.page_accent(title["href"]),
                    "scrapper_at": datetime.utcnow().isoformat()
                })
                if count2 == count:
                    break
                count2 += 1

            driver.quit()
            print("✅ Se realizo el webscraping del acento con exito")
            return self.news
        
        except:
            print("❌ No se pudo completar el webscraping de acento.")
