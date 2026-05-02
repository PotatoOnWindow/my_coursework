# пока простой in-memory storage

saved_articles = []


def save_article(article):
    if article not in saved_articles:
        saved_articles.append(article)


def get_saved():
    return saved_articles
