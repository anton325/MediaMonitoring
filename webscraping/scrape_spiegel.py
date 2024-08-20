import webscraping.scrape as scrape

def scrape_spiegel():

    ARTICLE_TAG = "align-middle"
    CATEGORY_TAG = ".sm\\:mb-6"
    TITLE_TAG = "align-middle"
    LEADTEXT_TAG = "RichText"
    DATE_TAG = "time"

    return scrape.scrape_template(
        "https://www.spiegel.de/wirtschaft/",
        "[class={}]".format(ARTICLE_TAG),
        CATEGORY_TAG,
        "[class={}]".format(TITLE_TAG),
        "[class*={}]".format(LEADTEXT_TAG),
        DATE_TAG,
        "Spiegel.de"
    )




if __name__ == "__main__":
    scrape_spiegel()