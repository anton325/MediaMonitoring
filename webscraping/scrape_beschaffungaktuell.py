from webscraping.dataclass_article import Article, custom_print_articles
import webscraping.scrape as scrape


def scrape_beschaffungaktuell():

    ARTICLE_TAG = "entry-title"
    CATEGORY_TAG = "meta-category"
    TITLE_TAG = "entry-title"
    LEADTEXT_TAG = "single__excerpt"
    DATE_TAG = "updated"


    return scrape.scrape_template(
        "https://beschaffung-aktuell.industrie.de/",
        "[class*={}]".format(ARTICLE_TAG),
        "[class={}]".format(CATEGORY_TAG),
        "[class*={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        "[class={}]".format(DATE_TAG),
        "Beschaffung-Aktuell",
        [],
        48
    )




if __name__ == "__main__":
    scrape_beschaffungaktuell()