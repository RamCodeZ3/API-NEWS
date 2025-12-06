# 📰 API-News
API-News es una **API con Python en FastAPI** que realiza **web scraping** de los principales periódicos digitales de la República Dominicana:

- **Diario Libre**
- **Acento**
- **El Nuevo Diario**

El objetivo es ofrecer un **endpoint unificado** para obtener noticias frescas desde diferentes fuentes, procesadas mediante **Selenium** y **BeautifulSoup (bs4)**.

---

## 🚀 Características
- ✔️ Webscraping dinámico con **Selenium**
- ✔️ Parsing de contenido con **BeautifulSoup**
- ✔️ API rápida y documentada con **FastAPI**
- ✔️ Soporte para múltiples fuentes
- ✔️ Opciones para elegir cuántos artículos obtener
- ✔️ Endpoints claros y fáciles de consumir

---

## 📂 Estructura del Proyecto

```
📦 API-News
┃
┣ 📂 src
┃ ┣ 📂 scrappers
┃ ┃ ┣ 📂 scrapper_accent
┃ ┃ ┃ ┣ accent.py
┃ ┃ ┃ ┣ page_accent.py
┃ ┃ ┣ 📂 scrapper_free_diary
┃ ┃ ┃ ┣ free_diary.py
┃ ┃ ┃ ┣ page_free_diary.py
┃ ┃ ┣ 📂 scrapper_the_new_diary
┃ ┃ ┃ ┣ the_new_diary.py
┃ ┃ ┃ ┣ page_the_new_diary.py
┃ ┣ main.py  # Archivo principal de la API
┃
┣ 📜 requirements.txt
┣ 📜 README.md
┣ 📜 LICENSE
┗ 📜 .gitignore
```

---

## 🌐 Endpoints Disponibles

### **1️⃣ Obtener noticias por fuente y cantidad**
```
GET /news/scrapper/{source}/{count}
```

### **Parámetros**
| Parámetro | Tipo | Descripción |
|----------|------|--------------|
| `source` | string | Fuente a consultar: `diarioLibre`, `acento`, `elNuevoDiario` |
| `count`  | int | Cantidad de artículos a devolver |

### **Ejemplo**
```
GET /news/scrapper/elNuevoDiario/5
```

---

### **2️⃣ Obtener todos los scrappers**
```
GET /news/scrappers/
```

---

## 🛠️ Tecnologías usadas
- **Python 3**
- **FastAPI**
- **Selenium WebDriver**
- **BeautifulSoup (bs4)**
- **Requests**
- **Uvicorn** (para ejecutar la API)

---

## 📥 Instalación y ejecución

### 1. Clona el repositorio
```bash
git clone https://github.com/tuusuario/api-news.git
cd api-news
```

### 2. Instila las dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecuta la API
```bash
uvicorn src.main:app --reload
```

### 4. Accede a la documentación interactiva
🌐 **Swagger UI:**  
```
http://127.0.0.1:8000/docs
```

🌐 **ReDoc:**  
```
http://127.0.0.1:8000/redoc
```

---

## 📄 Ejemplo de respuesta

```json
{
  "message": "Noticias conseguida con exito",
  "scrapper_news": [
    {
      "source_information": "Diario Libre",
      "category": "Actualidad",
      "title": "Hubo un incendio en el norte del pais",
      "link": "https://www.diariolibre.com/incendio",
      "summary": "descripcion",
      "scrapper_at": "2025-12-06T03:27:37.527687"
    }
  ]
}
```

---

## 📌 Notas importantes
- Selenium requiere un driver (ChromeDriver o GeckoDriver).
- Las páginas pueden cambiar, por lo que la estructura del scraping puede necesitar ajustes en el futuro.
- Usar responsablemente los scrappers para no saturar los sitios web.

---

## 📝 Licencia
Este proyecto está bajo la licencia **MIT**.
