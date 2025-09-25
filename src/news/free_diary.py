from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

URL = "https://www.diariolibre.com/ultima-hora"

class FreeDiary:
    def __init__(self):
        self.news = []

    def news_free_diary(self):
        # Configuración de Chrome en modo headless
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Abrir navegador (Chrome)
        driver = webdriver.Chrome(options=options)
        driver.get(URL)

        # Esperar a que cargue el JS
        time.sleep(5)

        # Obtener HTML ya renderizado
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Buscar artículos
        articles = soup.select("article")

        for art in articles:
            title = art.select_one("h2 a")
            resumen = art.select_one("p.hidden.sm\\:block")
            img = art.select_one("img")

            self.news.append({
                'Title': title.get_text(strip=True) if title else None,
                'Link': "https://www.diariolibre.com" + title["href"] if title else None,
                'Resumen': resumen.get_text(strip=True) if resumen else None,
                'Image': img["src"] if img else None
            })

        driver.quit()
        return self.news
