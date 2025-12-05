from fastapi import FastAPI
from datetime import datetime
from scrappers.scrapper_free_diary.free_diary import FreeDiary
from scrappers.scrapper_daily_list.daily_list import DailyList
from scrappers.scrapper_the_caribbean.the_caribbean import TheCaribbean
from scrappers.scrapper_accent.accent import Accent
from scrappers.scrapper_the_new_diary.the_new_diary import TheNewDiary

scrapper_FreDiary = FreeDiary()
scrapper_DailyList = DailyList()
scrapper_TheCaribbean = TheCaribbean()
scrapper_accent = Accent()
scrapper_the_new_diary = TheNewDiary()
app = FastAPI()

@app.get("/news/scrapper/{source}/{count}")
async def get_news_from_scrapper(source: str, count: int):
    print(f'🎬 Se comenzo con el webscraping de {source} ✅')
    
    if source == 'diarioLibre':
        data_new = scrapper_FreDiary.news_free_diary(count)
    
    elif source == 'listinDiario':
        data_new = scrapper_DailyList.news_daily_list(count)
    
    elif source == 'elCariber':
        data_new = scrapper_TheCaribbean.news_the_carribean(count)
    
    elif source == 'acento':
        data_new = scrapper_accent.news_accent(count)
    
    elif source == 'elNuevoDiario':
        data_new = scrapper_the_new_diary.news_the_new_diary(count)
    
    else:
        return{"message": f'La API no contiene informacion de esta "{source}" fuente'}
    
    print('🎬 Se obtuvo los datos exitosamente ✅')
    created_news = []

    for news_item in data_new:
        news_data = {
            "source_information": news_item.get("source_information"),
            "category": news_item.get("category"),
            "title": news_item.get("title"),
            "summary": news_item.get("summary"),
            "url_information": news_item.get("link"),
            "scrapper_at": datetime.utcnow().isoformat()
        }
        
        created_news.append(news_data)

    print('🎬 Webscraping finalizado con exito ✅')
    return {"message": "Noticias conseguida con exito", "created_news": created_news}
