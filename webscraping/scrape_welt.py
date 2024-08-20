import webscraping.scrape as scrape

def scrape_welt():

    ARTICLE_TAG = "c-teaser__headline-link"
    CATEGORY_TAG = "rf-o-topic"
    TITLE_TAG = "c-headline"
    LEADTEXT_TAG = "c-summary__intro"
    DATE_TAG = "time"

    return scrape.scrape_template(
        "https://www.welt.de/wirtschaft/",
        "[class*={}]".format(ARTICLE_TAG),
        "[class*={}]".format(CATEGORY_TAG),
        "[class*={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        DATE_TAG,
        "WELT",
        [],
        40
    )




if __name__ == "__main__":
    scrape_welt()