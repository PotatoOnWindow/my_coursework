import flet as ft
from services.api_client import get_news


def home_view(page: ft.Page, open_article):

    news_list = ft.Column()

    def load(e=None):
        news_list.controls.append(ft.Text("LOADING..."))
        page.update()

        try:
            news = get_news()
            
            print(news)

            news_list.controls.clear()

            for item in news:
                if "id" not in item:
                    news_list.controls.append(ft.Text(f"BAD ITEM: {item}"))
                    continue

                news_list.controls.append(
                    ft.Card(
                        content=ft.ListTile(
                            title=ft.Text(item["title"]),
                            subtitle=ft.Text(item.get("source", "")),
                            on_click=lambda e, id=item["id"]: open_article(id)
                        )
                    )
                )

            page.update()

        except Exception as e:
            news_list.controls.append(ft.Text(f"ERROR: {e}"))
            page.update()

    # 👉 кнопка вместо авто-загрузки
    return ft.Column([
        ft.ElevatedButton("Load news", on_click=load),
        news_list
    ])
