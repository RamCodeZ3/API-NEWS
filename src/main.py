from fastapi import FastAPI
from datetime import datetime
from scrappers.scrapper_free_diary.free_diary import FreeDiary
from supabase.supabase import supabase
scrapper = FreeDiary()

data_new = scrapper.news_free_diary()

app = FastAPI()

@app.post("/news/scrapper")
def add_news_from_scrapper(data_new: list[dict]):
    created_news = []

    for news_item in data_new:
        news_data = {
            "source_information": news_item.get("source_information"),
            "title": news_item.get("title"),
            "summary": news_item.get("summary"),
            "url_information": news_item.get("link"),
            "url_image": news_item.get("url_link"),
            "created_at": datetime.utcnow().isoformat()
        }

        response = supabase.table("news").insert(news_data).execute()
        if response.data:
            created_news.append(response.data[0])

    return {"message": "Noticias agregadas", "created_news": created_news}

add_news_from_scrapper(data_new) 
