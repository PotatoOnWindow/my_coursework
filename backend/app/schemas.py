from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NewsBase(BaseModel):
    title: str
    content: str
    source: Optional[str] = None
    url: Optional[str] = None
    tags: Optional[str] = None


class NewsCreate(NewsBase):
    pass


class NewsOut(NewsBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # важно для TortoiseORM
