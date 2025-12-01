from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from scrappers.scrapper_daily_list.page_daily_list import PageDailyList


URL = "https://listindiario.com/search/?query=ultima+hora"
scrapper = PageDailyList()

class DailyList:
    def __init__(self):
        self.news = []
    
    def news_daily_list(self, count: int):
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

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        articles = soup.select("article")
        count2 = 1

        for art in articles:
            title = art.select_one("h3 a")
            img = art.select_one("figure picture img")
            link = 'https://listindiario.com' + title['href']

            self.news.append({
                "source_information": "Listin Diario",
                'title': title.get_text(strip=True) if title else None,
                'link': link,
                'summary': scrapper.page_daily_list(
                    "https://listindiario.com" + title["href"]
                    ),
                'url_img': img["src"] if img else None
            })
            if count2 == count:
                break
            count2 += 1
        
        driver.quit()
        return self.news
