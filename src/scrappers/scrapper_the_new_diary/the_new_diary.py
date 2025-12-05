from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from scrappers.scrapper_the_new_diary.page_the_new_diary import PageTheNewDiary


URL = "https://elnuevodiario.com.do/novedades/"
scrapper = PageTheNewDiary()

class TheNewDiary:
    def __init__(self):
        self.news = []
    
    def news_the_new_diary(self, count: int):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        service = Service(log_path='NUL')
        driver = webdriver.Chrome(options=options, service=service)
        driver.set_page_load_timeout(60)
        driver.implicitly_wait(10)
        driver.get(URL)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        articles = soup.select("article")
        count2 = 1

        for art in articles:
            title = art.select_one("div div header a")
            category = None

            self.news.append({
                "source_information": "El Nuevo Diario",
                "category": category,
                'title': title.get_text(strip=True) if title else None,
                'link': title["href"],
                'summary': scrapper.page_the_new_diary(title["href"])
            })
            if count2 == count:
                break
            count2 += 1
        
        driver.quit()
        return self.news
