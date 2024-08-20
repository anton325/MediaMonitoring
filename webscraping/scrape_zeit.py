from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# from webscraping.dataclass_article import Article, custom_print_articles
# import webscraping.scrape as scrape
# import date_parser
# def scrape_zeit():

ARTICLE_TAG = "[class*='z']"#"zon-teaser-lead__heading-link"
CATEGORY_TAG = "article-heading__kicker"
TITLE_TAG = "article-heading__title "
LEADTEXT_TAG = "summary"
DATE_TAG = ""

#single__date

    # return scrape.scrape_template(
    #     "https://www.zeit.de/index",
    #     "[class={}]".format(ARTICLE_TAG),
    #     "[class={}]".format(CATEGORY_TAG),
    #     "[class={}]".format(TITLE_TAG),
    #     "[class={}]".format(LEADTEXT_TAG),
    #     DATE_TAG
    # )




# if __name__ == "__main__":
#     scrape_zeit()

def scrape_template(website_link, article_tag, category_tag, title_tag, leadtext_tag, date_tag):

    options = Options()
    # options.add_argument("--headless=new")
    # options.add_argument("--window-size=1920,1200")
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)#, executable_path=DRIVER_PATH)
    driver.implicitly_wait(4)
    Articles = []
    articles_clicked = []
    articles_scraped = 0

    if "zeit" in website_link:
        driver.get(website_link)
        time.sleep(2)
        button = driver.find_elements(By.TAG_NAME,"button")
        for b in button:
            print(b.get_attribute("textContent"))
        # button.click()

    while articles_scraped < 15:
        driver.get(website_link)
        time.sleep(2)

        elements = driver.find_elements(By.CSS_SELECTOR,article_tag)

        print("Number of articles on page: {}".format(len(elements))) 

        if len(elements) == len(articles_clicked):
            break
        

        for e in elements:
            which_attribute = "textContent"
            if e.get_attribute(which_attribute) == "":
                which_attribute = "href"
            element_identifier = e.get_attribute(which_attribute)
            print(element_identifier)
            if element_identifier in articles_clicked:
                # print("continue {}".format(element_identifier))
                continue
            articles_scraped += 1
            articles_clicked.append(element_identifier)
            # print(e.text)

            # driver.execute_script('arguments[0].click()', e)
            
            # try:
            #     print("On: {}".format(driver.current_url))
            #     kicker = driver.find_element(By.CSS_SELECTOR,category_tag).get_attribute("textContent")
            #     title = driver.find_element(By.CSS_SELECTOR,title_tag).get_attribute("textContent")
            #     leadtext = driver.find_element(By.CSS_SELECTOR,leadtext_tag).get_attribute("textContent")
            #     date = driver.find_element(By.CSS_SELECTOR,date_tag).get_attribute("textContent")
            #     date = date_parser.parse_date(date)
            #     kicker,title,leadtext = strip_strings(kicker,title,leadtext)
            #     link = driver.current_url
            #     thisArticle = Article(kicker,title,leadtext,link,date)
            #     Articles.append(thisArticle)
            #     custom_print_articles(Articles)
            # except Exception as e:
            #     print(e)
            #     pass
            # break
        
    return Articles

if __name__ == "__main__":
    scrape_template(
            "https://www.zeit.de/wirtschaft/index",
            ARTICLE_TAG,
            "[class={}]".format(CATEGORY_TAG),
            "[class={}]".format(TITLE_TAG),
            "[class={}]".format(LEADTEXT_TAG),
            DATE_TAG,
        )