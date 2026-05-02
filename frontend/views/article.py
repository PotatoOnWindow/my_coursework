import flet as ft
from services.api_client import get_article

def article_view(page: ft.Page, news_id: int, go_back):
    view = ft.Column()

    def load():
        def worker():
            article = get_article(news_id)

            view.controls.clear()

            view.controls.append(
                ft.Text(article.get("title", "No title"), size=22)
            )

            view.controls.append(
                ft.Text(article.get("content", "No content"))
            )

            view.controls.append(
                ft.ElevatedButton("← Back", on_click=lambda e: go_back())
            )

            page.update()

        threading.Thread(target=worker).start()

    load()

    return view
