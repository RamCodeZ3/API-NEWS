from fastapi import FastAPI
from scrappers.scrapper_free_diary.free_diary import FreeDiary
from scrappers.scrapper_accent.accent import Accent
from scrappers.scrapper_the_new_diary.the_new_diary import TheNewDiary


scrapper_FreDiary = FreeDiary()
scrapper_accent = Accent()
scrapper_the_new_diary = TheNewDiary()
app = FastAPI()


@app.get("/news/scrapper/{source}/{count}")
async def get_news_from_scrapper(source: str, count: int):
    print(f'Se inicializo el webscraping de {source} ✅')
    
    if source == 'diarioLibre':
        data_new = await scrapper_FreDiary.news_free_diary(count)
    
    elif source == 'acento':
        data_new = await scrapper_accent.news_accent(count)
    
    elif source == 'elNuevoDiario':
        data_new = await scrapper_the_new_diary.news_the_new_diary(count)
    
    else:
        return{
            "message": f'La API no contiene informacion de esta "{source}" fuente'
        }
    
    print('Webscraping finalizado con exito ✅')
    return {
        "message": "Noticias conseguida con exito",
        "scrapper_news": data_new
    }

@app.get("/news/scrappers/")
async def get_all_news_scrapper():
    print(f'Se inicializo el webscraping ✅')
    news = []
    news.append(await scrapper_FreDiary.news_free_diary(5))
    
    news.append(await scrapper_accent.news_accent(5))
    
    news.append(await scrapper_the_new_diary.news_the_new_diary(5))
    
    return {
        "message": "Noticias conseguida con exito",
        "scrapper_news": news
    }
