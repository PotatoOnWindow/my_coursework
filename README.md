# my_coursework
android app with backend + parser of news websites

how to make pkg... idk yet

## Structure of files:

backend/
    main.py                 *точка входа FastAPI*
    models.py               *TortoiseORM*
    schemas.py              *Pydantic-схемы (что это значит?)*
    routes/                 *-- эндпоинты*
        news.py             *новостные статьи*
        search.py           *поиск*
    services/               *-- логика*
        news_service.py     *работа с новостями*
        parser_service.py   *взаимодействие с парсером*
    db/                     *-- базы данных*
        config.py           *подключение к БД*
        init.py             *инициализация БД*
    utils/                  
        helpers.py          *вспомогательные функции*
    requirements.txt

frontend/
    main.py                 *запуск Flet-приложения*
    views/
        home.py             *список новостей*
        article.py          *просмотр статьи*
        search.py           *поисковая строка/поиск*
    components/
        news_card.py        
        search_bar.py
    services/
        api_client.py       *работа с FastAPI*
    storage/
        offline             *сохранение статей*

parser/
    main.py
    parsers/
        base_parser.py
        website1.py
        website2.py
    utils.py
    requirements.txt

shared/                     *-- общие настройки (URL, API)*
    config.py               
    constants.py

README.md
.gitignore
