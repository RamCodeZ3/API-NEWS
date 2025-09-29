from fastapi import FastAPI
from supabase_client import supabase
from datetime import datetime
from news.free_diary import FreeDiary
scrapper = FreeDiary

data_new = scrapper.news_free_diary

app = FastAPI()

@app.post("/news/scraper")
def add_news_from_scraper(data_new: list[dict]):
    created_news = []

    for news_item in data_new:
        news_data = {
            "source_information": news_item.get("source_information"),
            "title": news_item.get("title"),
            "summary": news_item.get("summary"),
            "url_information": news_item.get("link"),
            "url_image": news_item.get("url_link"),
            "created_at": datetime.utcnow()
        }

        # Insertar en Supabase
        response = supabase.table("news").insert(news_data).execute()
        if response.data:
            created_news.append(response.data[0])

    return {"message": "Noticias agregadas", "created_news": created_news}
