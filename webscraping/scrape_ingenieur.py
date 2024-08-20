from webscraping.dataclass_article import Article, custom_print_articles
import webscraping.scrape as scrape


def scrape_ingenieur():

    ARTICLE_TAG = "ing-teaser__link"
    CATEGORY_TAG = "single__subheadline"
    TITLE_TAG = "single__title"
    LEADTEXT_TAG = "single__excerpt"
    DATE_TAG = "single__date"

#single__date

    return scrape.scrape_template(
        "https://www.ingenieur.de/",
        "[class={}]".format(ARTICLE_TAG),
        "[class={}]".format(CATEGORY_TAG),
        "[class*={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        "[class={}]".format(DATE_TAG),
        "Ingenieur.de"
    )




if __name__ == "__main__":
    scrape_ingenieur()