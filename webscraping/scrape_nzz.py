import webscraping.scrape as scrape

def scrape_nzz():

    ARTICLE_TAG = "teaser__title-name" #"teaser__title"
    #CATEGORY_TAG = "teaser__flag--text"
    CATEGORY_TAG = "headline__title"
    TITLE_TAG = "headline__title"
    LEADTEXT_TAG = "headline__lead"
    DATE_TAG = "time"

    return scrape.scrape_template(
        "https://www.nzz.ch/deutschland/wirtschaft",
        "[class*={}]".format(ARTICLE_TAG),
        "[class={}]".format(CATEGORY_TAG),
        "[class={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        DATE_TAG,
        "NZZ",
        ["https://www.nzz.ch/deutschland/wirtschaft"]
    )




if __name__ == "__main__":
    scrape_nzz()