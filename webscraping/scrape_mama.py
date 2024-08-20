import webscraping.scrape as scrape

def scrape_mama():

    ARTICLE_TAG = ".hover\\:opacity-moderate"
    CATEGORY_TAG = ".sm\\:mb-6"
    TITLE_TAG = "align-middle"
    LEADTEXT_TAG = "RichText"
    DATE_TAG = "timeformat"

    return scrape.scrape_template(
        "https://www.manager-magazin.de/",
        ARTICLE_TAG,
        CATEGORY_TAG,
        "[class={}]".format(TITLE_TAG),
        "[class*={}]".format(LEADTEXT_TAG),
        "[class={}]".format(DATE_TAG),
        "Manager-Magazin"
    )
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# from dataclass_article import Article, custom_print_articles

# def scrape_template(website_link, article_tag, category_tag, title_tag, leadtext_tag):

#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--window-size=1920,1200")
#     # options.add_experimental_option("detach", True)

#     driver = webdriver.Chrome(options=options)#, executable_path=DRIVER_PATH)
#     driver.implicitly_wait(5)
#     Articles = []
#     articles_clicked = []

#     while True:
#         driver.get(website_link)
#         time.sleep(3)

#         elements = driver.find_elements(By.CSS_SELECTOR,".hover\\:opacity-moderate")

#         # print("Number of articles on page: {}".format(len(elements))) 

#         if len(elements) == len(articles_clicked):
#             break
        

#         for e in elements:
#             text_content = e.get_attribute("textContent")
#             if text_content in articles_clicked:
#                 continue
#             # print(e.get_attribute('class'))
#             # print(e.get_attribute("textContent"))
#             articles_clicked.append(e.get_attribute("textContent"))
#             # print(e.text)

#             driver.execute_script('arguments[0].click()', e)
#             try:
#                 #kicker = driver.find_element(By.CSS_SELECTOR,"[class*={}]".format(category_tag)).get_attribute("textContent")
#                 kicker = driver.find_element(By.CSS_SELECTOR,".sm\\:mb-6").get_attribute("textContent")
#                 kicker = kicker.strip()
#                 # print(kicker)
#                 title = driver.find_element(By.CSS_SELECTOR,"[class={}]".format(title_tag)).get_attribute("textContent")
#                 title = title.strip()
#                 # print(title)
#                 leadtext = driver.find_element(By.CSS_SELECTOR,"[class*={}]".format(leadtext_tag)).get_attribute("textContent")
#                 leadtext = leadtext.strip()
#                 # print(leadtext)
                
#                 link = driver.current_url
#                 thisArticle = Article(kicker,title,leadtext,link)
#                 Articles.append(thisArticle)
#                 custom_print_articles(Articles)
#             except Exception as e:
#                 print(e)

#                 pass
#             break
        
#     return Articles

if __name__ == "__main__":
    scrape_manager_magazin()