from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from utils.nlp_pipeline import summarizer_article
import time

class PageFreeDiary:
    def __init__(self):
        self.summary = ""

    def page_free_diary(self, url):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        article = soup.find("div", class_="detail-body")
        paragraphs = article.find_all("p")

        self.summary = " ".join(p.get_text(
            " ",
            strip=True) for p in paragraphs)
        
        driver.quit()
        return summarizer_article(self.summary)

