import webscraping.scrape as scrape

def scrape_industryofthings():

    ARTICLE_TAG = "inf-headline-3"
    CATEGORY_TAG = "inf-subhead-1"
    TITLE_TAG = "inf-headline-1"
    LEADTEXT_TAG = "inf-text--large"
    DATE_TAG = "inf-date"

    return scrape.scrape_template(
        "https://www.industry-of-things.de/",
        "[class={}]".format(ARTICLE_TAG),
        "[class*={}]".format(CATEGORY_TAG),
        "[class*={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        "[class={}]".format(DATE_TAG),
        "Industry-of-things",
        [],
        custom_limit=60,
        skip_first=0
    )




if __name__ == "__main__":
    scrape_industryofthings()