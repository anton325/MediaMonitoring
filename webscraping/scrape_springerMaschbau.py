import webscraping.scrape as scrape

def scrape_springermaschbau():

    ARTICLE_TAG = "m-universal-teaser__headline"
    CATEGORY_TAG = "rf-ic"
    TITLE_TAG = "h1"
    LEADTEXT_TAG = "c-summary__intro"
    DATE_TAG = "time"

    return scrape.scrape_template(
        "https://www.springerprofessional.de/maschinenbau-werkstoffe/6636654",
        "[class={}]".format(ARTICLE_TAG),
        "[class*={}]".format(CATEGORY_TAG),
        TITLE_TAG,
        "[class={}]".format(LEADTEXT_TAG),
        DATE_TAG,
        "Springer-Professional",
        [],
        40
    )




if __name__ == "__main__":
    scrape_springermaschbau()