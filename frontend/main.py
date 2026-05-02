import flet as ft

import threading

from views.home import home_view
from views.article import article_view
from storage.offline import get_saved
from services import api_client

import traceback

print("MAIN STARTED")

def main(page: ft.Page):
    page.title = "News App"

    content = ft.Column()
   
   # for debug
    try: 
        page.add(ft.Text("APP STARTED"))

    # ---------------- NAV ----------------

        def set_view(view):
            content.controls.clear()
            content.controls.append(view)
            page.update()


        def open_home():
            set_view(home_view(page, open_article))


        def open_article(news_id):
            set_view(article_view(page, news_id, open_home))


        def open_saved(e=None):
            saved = get_saved()

            col = ft.Column([
                ft.Text("Saved Articles", size=20),
            ])

            for article in saved:
                col.controls.append(ft.Text(article["title"]))

            set_view(col)


        def open_settings(e=None):
            url_field = ft.TextField(
                label="BASE_URL",
                value=api_client.BASE_URL
            )

            col = ft.Column([
                ft.Text("Settings", size=20),
                url_field,
                ft.ElevatedButton(
                    "Save",
                    on_click=lambda e: setattr(api_client, "BASE_URL", url_field.value)
                )
            ])

            set_view(col)

        # ---------------- DRAWER ----------------

        def on_drawer_change(e):
            index = e.control.selected_index
            page.drawer.open = False

            if index == 0:
                set_view(home_view(page, open_article)) 
            elif index == 1:
                open_saved()
            elif index == 2:
                open_settings()
            page.update()


        page.drawer = ft.NavigationDrawer(
                on_change=on_drawer_change,
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.HOME,
                    label="Home",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.BOOKMARK,
                    label="Saved Articles",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.SETTINGS,
                    label="Settings",
                ),
            ]
        )


        def open_drawer(e):
            page.drawer.open = True
            page.update()


        page.appbar = ft.AppBar(
            title=ft.Text("News App"),
            leading=ft.IconButton(
                icon=ft.Icons.MENU,
                on_click=open_drawer
            )
        )

        page.add(content)
        open_home()

    except Exception as e:
        page.add(ft.Text(str(e)))
        print(traceback.format_exc())


ft.app(target=main)
