try:
    import webscraping.scrape as scrape
except:
    import scrape


def scrape_handelsblatt():

    ARTICLE_TAG = "bold"
    CATEGORY_TAG = "app-header-content-kicker" # "title" # "kicker"
    TITLE_TAG = "app-header-content-headline" # "headline"
    LEADTEXT_TAG = "app-header-content-lead-text" #"lead-text"
    DATE_TAG = "app-story-date"

    
    return scrape.scrape_template(
        "https://www.handelsblatt.com/",
        "[class*={}]".format(ARTICLE_TAG),
        # "[class*={}]".format(CATEGORY_TAG),
        CATEGORY_TAG,
        #"[class={}]".format(TITLE_TAG),
        TITLE_TAG,
        #"[class={}]".format(LEADTEXT_TAG),
        LEADTEXT_TAG,
        DATE_TAG,
        "Handelsblatt",
        custom_limit=40,
    )

if __name__ == "__main__":
    scrape_handelsblatt()