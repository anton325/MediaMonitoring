try:
    import webscraping.scrape as scrape
except:
    import scrape

def scrape_faz():

    ARTICLE_TAG = "tsr-Base_HeadlineText"
    CATEGORY_TAG = "atc-HeadlineEmphasisText"
    TITLE_TAG = "atc-HeadlineText"
    LEADTEXT_TAG = "atc-IntroText"
    DATE_TAG = "atc-MetaTime"

    return scrape.scrape_template(
        "https://www.faz.net/aktuell/wirtschaft/",
        "[class={}]".format(ARTICLE_TAG),
        "[class={}]".format(CATEGORY_TAG),
        "[class={}]".format(TITLE_TAG),
        "[class={}]".format(LEADTEXT_TAG),
        "[class={}]".format(DATE_TAG),
        "FAZ",
        ['https://www.faz.net/aktuell/'],
        40
    )

# avoid: https://www.faz.net/aktuell/ -> muss genau diese Länge haben, es gibt auch Artikel, die mit https://www.faz.net/aktuell/ anfangen



if __name__ == "__main__":
    scrape_faz()