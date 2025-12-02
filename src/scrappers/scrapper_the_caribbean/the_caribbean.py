from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from scrappers.scrapper_the_caribbean.page_the_caribbean import PageTheCaribbean


URL = "https://www.elcaribe.com.do/autor/elcaribe/"
scrapper = PageTheCaribbean()

class TheCaribbean:
    def __init__(self):
        self.news = []
    
    def news_the_carribean(self, count: int):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        service = Service(log_path='NUL')
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(URL)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        articles = soup.select('article')
        count2 = 1

        for art in articles:
            category = art.select_one('div.entry-content-wrap header div a')
            title = art.select_one('div.entry-content-wrap header h3 a')
            link = title['href']
            img = art.select_one('a div div img')

            self.news.append({
                "source_information": "El Caribe",
                "category": category.get_text(strip=True),
                'title': title.get_text(strip=True) if title else None,
                'link': link,
                'summary': scrapper.page_the_caribbean(
                    title["href"]
                    ),
                'url_img': img["src"] if img else None
            })
            
            if count2 == count:
                break
            count2 += 1
        
        driver.quit()


