from webscraping.dataclass_article import Article, custom_print_articles
import webscraping.scrape as scrape


def scrape_deutschlandfunk():

    ARTICLE_TAG = "headline-title"
    CATEGORY_TAG = "headline-kicker"
    TITLE_TAG = "headline-title"
    LEADTEXT_TAG = "article-header-description"
    DATE_TAG = "article-header-author"

#single__date

    return scrape.scrape_template(
        "https://www.deutschlandfunk.de/wirtschaft-106.html",
        "[class={}]".format(ARTICLE_TAG),
        "[class={}]".format(CATEGORY_TAG),
        "[class={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        "[class={}]".format(DATE_TAG),
        "Deutschlandfunk",
        [],
        50
    )

if __name__ == "__main__":
    scrape_deutschlandfunk()