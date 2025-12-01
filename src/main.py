from fastapi import FastAPI
from datetime import datetime
from scrappers.scrapper_free_diary.free_diary import FreeDiary
from scrappers.scrapper_daily_list.daily_list import DailyList

scrapper_FreDiary = FreeDiary()
scrapper_DailyList = DailyList()
app = FastAPI()

@app.get("/news/scrapper/{source}/{count}")
async def get_news_from_scrapper(source: str, count: int):
    print('🎬 Se comenzo con el webscraping ✅')
    
    if source == 'FreeDiary':
        data_new = scrapper_FreDiary.news_free_diary(count)
    
    elif source == 'DailyList':
        data_new = scrapper_DailyList.news_daily_list(count)
    
    print('🎬 Se obtuvo los datos exitosamente ✅')
    created_news = []

    for news_item in data_new:
        news_data = {
            "source_information": news_item.get("source_information"),
            "title": news_item.get("title"),
            "summary": news_item.get("summary"),
            "url_information": news_item.get("link"),
            "url_image": news_item.get("url_link"),
            "scrapper_at": datetime.utcnow().isoformat()
        }
        
        created_news.append(news_data)

    print('🎬 Webscraping finalizado con exito ✅')
    return {"message": "Noticias agregadas", "created_news": created_news}
