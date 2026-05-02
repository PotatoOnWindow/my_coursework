from fastapi import APIRouter
from typing import List

from app.models import News
from app.schemas import NewsOut

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("/", response_model=List[NewsOut])
async def search_news(query: str):
    return await News.filter(title__icontains=query).all()
