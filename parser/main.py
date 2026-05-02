import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def get_html(url: str):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # ждём базовую загрузку
    time.sleep(2)

    # пролистывание для lazy-load элементов
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)

        new_height = driver.execute_script("return document.body.scrollHeight")

        # если дальше не кроллится
        if new_height == last_height:
            break
        last_height = new_height
    
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, ".article__body p")) >= 8
    )

    prev_text_len = 0
    for _ in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)

        paragraphs = driver.find_elements(By.CSS_SELECTOR, ".article__body p")
        current_len = len(paragraphs)

        if current_len == prev_text_len:
            break
        prev_text_len = current_len


    html = driver.page_source
    driver.quit()

    return html


def parse_article(url: str):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("h1", class_="article__title")
    subtitle = soup.find("p", class_="article__subtitle")
    body = soup.find("div", class_="article__body")

    paragraphs = [p.text.strip() for p in body.find_all("p")] if body else []

    # debug
    print("PARAGRAPHS: ", len(body.find_all("p")) if body else 0)

    return {
        "title": title.text.strip() if title else "",
        "subtitle": subtitle.text.strip() if subtitle else "",
        "content": "\n\n".join(paragraphs),
    }


if __name__ == "__main__":
    url = "https://www.mk.ru/politics/2026/05/01/premer-evropeyskoy-strany-prerval-pervomayskuyu-rech-izza-protestuyushhikh.html"
    article = parse_article(url)

    print(article["title"])
    print(article["content"][:500])
    
