from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


class PageTheCaribbean:
    def __init__(self):
        self.summary = ""

    def page_the_caribbean(self, url):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        service = Service(log_path='NUL')
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(url)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")

        article = soup.select('article div div.content')

        if article is None:
            print("No se encontró el artículo en:", url)
            return "Artículo no disponible"
        
        paragraphs = article.find_all("p")

        self.summary = " ".join(p.get_text(
            " ",
            strip=True) for p in paragraphs)
        
        driver.quit()
        print(self.summary)
        return self.summary

