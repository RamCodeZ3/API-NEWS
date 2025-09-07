from selenium import webdriver
from bs4 import BeautifulSoup
import time

URL = "https://www.diariolibre.com/ultima-hora"

# Abrir navegador (Chrome)
driver = webdriver.Chrome()
driver.get(URL)

# Esperar a que cargue el JS
time.sleep(5)

# Obtener HTML ya renderizado
soup = BeautifulSoup(driver.page_source, "html.parser")

# Ahora sí busca los artículos
articles = soup.select("article")

for art in articles:
    title = art.select_one("h2 a")
    
    if title:
        print("Título:", title.get_text(strip=True))
        print("Link:", title["href"])
    
    resumen = art.select_one("p.hidden.sm\\:block")
    
    if resumen:
        print("Resumen:", resumen.get_text(strip=True))
    print("--------------------------------------------------")

driver.quit()