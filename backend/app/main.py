from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.routes import news, search

app = FastAPI()


# Подключаем роуты
app.include_router(news.router)
app.include_router(search.router)


# Настройка базы данных
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def root():
    return {"message": "API is running"}
