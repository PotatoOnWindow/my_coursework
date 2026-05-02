from fastapi import APIRouter, HTTPException
from typing import List
from fastapi import HTTPException

from app.models import News
from app.schemas import NewsOut, NewsCreate

router = APIRouter(prefix="/news", tags=["News"])


# Получить все новости (список новостей)
@router.get("/", response_model=List[NewsOut])
async def get_all_news(limit: int = 10, offset: int = 0):
    return await News.all().order_by("-created_at").offset(offset).limit(limit)


# Добавить новость
@router.post("/", response_model=NewsOut)
async def create_news(news_data: NewsCreate):
    news = await News.create(**news_data.dict())
    return news


# Для новости, сохранённой в избранные, например. Сверху навесится ещё логика
@router.get("/{news_id}", response_model=NewsOut)
async def get_news(news_id: int):
    news = await News.get_or_none(id=news_id)

    if not news:
        raise HTTPException(status_code=404, detail="News not found")

    return news


# Удалить новость из бд
@router.delete("/{news_id}")
async def delete_news(news_id: int):
    news = await News.get_or_none(id=news_id)

    if not news:
        raise HTTPException(status_code=404, detail="News not found")
       # return {"error": "News not found"}

    await news.delete()
    return {"message": "News deleted"}


# Обновить новость в бд
@router.put("/{news_id}", response_model=NewsOut)
async def update_news(news_id: int, news_data: NewsCreate):
    news = await News.get_or_none(id=news_id)

    if not news: 
        raise HTTPException(status_code=404, detail="News not found")
       # return {"error": "News not found"}

    news.title = news_data.title
    news.content = news_data.content
    news.source = news_data.source
    news.url = news_data.url
    news.tags = news_data.tags

    await news.save()
    return news
