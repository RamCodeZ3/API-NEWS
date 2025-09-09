from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

URL = "https://www.diariolibre.com/ultima-hora"


class FreeDriary():
    def __init__(self, category: str, amount: int):
        self.amount = amount
        self.category = category
        options = Options()
        options.add_argument("--headless")         # Ejecuta sin abrir ventana
        options.add_argument("--disable-gpu")      # Recomendado en Windows
        options.add_argument("--no-sandbox")       # Útil en Linux
        options.add_argument("--disable-dev-shm-usage")

        # Abrir navegador (Chrome)
        driver = webdriver.Chrome(options=options)
        driver.get(URL)

        # Esperar a que cargue el JS
        time.sleep(5)

        # Obtener HTML ya renderizado
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Ahora sí busca los artículos
        articles = soup.select("article")

        for art in articles:
            title = art.select_one("h2 a")
            resumen = art.select_one("p.hidden.sm\\:block")
            img = art.select_one("img")

            if title:
                print("Título:", title.get_text(strip=True))
                print("Link:", "https://www.diariolibre.com" + title["href"])

            if resumen:
                print("Resumen:", resumen.get_text(strip=True))
                print(img["src"])
                break

        driver.quit()
