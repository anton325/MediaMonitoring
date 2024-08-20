import webscraping.scrape as scrape

def scrape_tagesschau():

    ARTICLE_TAG = "teaser__headline" #"teaser__title"
    #CATEGORY_TAG = "teaser__flag--text"
    CATEGORY_TAG = "seitenkopf__topline"
    TITLE_TAG = "seitenkopf__headline--text"
    LEADTEXT_TAG = "strong" #"headline__lead"
    DATE_TAG = "metatextline"

    return scrape.scrape_template(
        "https://www.tagesschau.de/wirtschaft",
        "[class={}]".format(ARTICLE_TAG),
        "[class={}]".format(CATEGORY_TAG),
        "[class={}]".format(TITLE_TAG),
        LEADTEXT_TAG,
        "[class={}]".format(DATE_TAG),
        "Tagesschau",
        [],
    )




if __name__ == "__main__":
    scrape_tagesschau()