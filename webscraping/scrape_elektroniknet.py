from webscraping.dataclass_article import Article, custom_print_articles
import webscraping.scrape as scrape


def scrape_elektroniknet():

    ARTICLE_TAG = "h2"
    CATEGORY_TAG = "article__overline"
    TITLE_TAG = "article__title"
    LEADTEXT_TAG = "article__bold"
    DATE_TAG = "article__time"

#single__date

    return scrape.scrape_template(
        "https://www.elektroniknet.de",
        ARTICLE_TAG,
        "[class={}]".format(CATEGORY_TAG),
        "[class={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        "[class={}]".format(DATE_TAG),
        "Elektroniknet.de",
        forbidden_sites = [],
        custom_limit = 40
    )




if __name__ == "__main__":
    scrape_elektroniknet()