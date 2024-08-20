import webscraping.scrape as scrape

def scrape_capital():

    ARTICLE_TAG = "teaser__headline"
    CATEGORY_TAG = "title__kicker"
    TITLE_TAG = "title__headline"
    LEADTEXT_TAG = "intro__text"
    DATE_TAG = "time"

    return scrape.scrape_template(
        "https://www.capital.de/",
        "[class*={}]".format(ARTICLE_TAG),
        "[class*={}]".format(CATEGORY_TAG),
        "[class*={}]".format(TITLE_TAG),
        "[class*={}]".format(LEADTEXT_TAG),
        DATE_TAG,
        "Capital",
        [],
        35
    )




if __name__ == "__main__":
    scrape_capital()