import webscraping.scrape as scrape

def scrape_produktion():

    ARTICLE_TAG = "headline"
    CATEGORY_TAG = "subline"
    TITLE_TAG = "title"
    LEADTEXT_TAG = "lead"
    DATE_TAG = "date"

    return scrape.scrape_template(
        "https://www.produktion.de/",
        "[class={}]".format(ARTICLE_TAG),
        "[class={}]".format(CATEGORY_TAG),
        "[class={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        "[class={}]".format(DATE_TAG),
        "Produktion.de"
    )

# avoid: https://www.faz.net/aktuell/ -> muss genau diese Länge haben, es gibt auch Artikel, die mit https://www.faz.net/aktuell/ anfangen



if __name__ == "__main__":
    scrape_produktion()