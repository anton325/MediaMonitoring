import webscraping.scrape as scrape

def scrape_tagesspiegel():

    ARTICLE_TAG = "VC2" #"teaser__title"
    CATEGORY_TAG = "Ncg"
    TITLE_TAG = "Nch"
    LEADTEXT_TAG = "By" #"headline__lead"
    DATE_TAG = "time"

    return scrape.scrape_template(
        "https://www.tagesspiegel.de/wirtschaft/",
        "[class={}]".format(ARTICLE_TAG),
        "[class={}]".format(CATEGORY_TAG),
        "[class={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        DATE_TAG,
        "Tagesspiegel",
        []
    )




if __name__ == "__main__":
    scrape_tagesspiegel()