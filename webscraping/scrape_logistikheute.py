import webscraping.scrape as scrape

def scrape_logistikheute():

    ARTICLE_TAG = "a"
    CATEGORY_TAG = "field--name-field-taxonomie"
    TITLE_TAG = "h1"
    LEADTEXT_TAG = "field--type-text-long"
    DATE_TAG = "field--name-node-post-date"

    return scrape.scrape_template(
        "https://logistik-heute.de/",
        ARTICLE_TAG,#"[class={}]".format(ARTICLE_TAG),
        "[class*={}]".format(CATEGORY_TAG),
        TITLE_TAG,
        "div[class*={}]".format(LEADTEXT_TAG),
        "[class*={}]".format(DATE_TAG),
        "Logistik-heute",
        [],
        custom_limit=23,
        skip_first=50
    )




if __name__ == "__main__":
    scrape_logistikheute()