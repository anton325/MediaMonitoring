import webscraping.scrape as scrape

def scrape_sz():

    # ARTICLE_TAG = "teaser-title"
    # ARTICLE_TAG = "sz-teaserlist-element"
    ARTICLE_TAG = "teaser-url"
    CATEGORY_TAG = "css-1tm5due" #"overline"
    TITLE_TAG = "css-1bhnxuf" #"title"
    LEADTEXT_TAG = "teaserText"
    DATE_TAG = "time"

    return scrape.scrape_template(
        "https://www.sueddeutsche.de/wirtschaft",
        "[data-manual*={}]".format(ARTICLE_TAG),
        #"[data-manual*={}]".format(CATEGORY_TAG),
        "[class*={}]".format(CATEGORY_TAG),
        #"[data-manual='{}']".format(TITLE_TAG),
        "[class*={}]".format(TITLE_TAG),
        "[data-manual='{}']".format(LEADTEXT_TAG),
        DATE_TAG,
        'Sueddeutsche',
        [],
        40
    )

if __name__ == "__main__":
    scrape_sz()