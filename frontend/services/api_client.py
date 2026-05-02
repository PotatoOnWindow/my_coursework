import httpx

BASE_URL = "http://192.168.0.103:8000"


def get_news():
    try:
        r = httpx.get(f"{BASE_URL}/news/", timeout=5.0)
        return r.json()
    except Exception as e:
        return [{"title": f"ERROR: {e}"}]


def get_article(news_id: int):
    try:
        r = httpx.get(f"{BASE_URL}/news/{news_id}", timeout=5.0)
        return r.json()
    except Exception as e:
        return {"title": "Error", "content": str(e)}
