import webscraping.scrape as scrape

def scrape_wiwo():

    ARTICLE_TAG = "js-headline"
    CATEGORY_TAG = "c-overline"
    TITLE_TAG = "c-headline"
    LEADTEXT_TAG = "c-leadtext"
    DATE_TAG = "time"

    return scrape.scrape_template(
        "https://www.wiwo.de/",
        "[class*={}]".format(ARTICLE_TAG),
        "[class*={}]".format(CATEGORY_TAG),
        "[class*={}]".format(TITLE_TAG),
        "[class*={}]".format(LEADTEXT_TAG),
        DATE_TAG,
        "WirtschaftsWoche"
    )



    # options = Options()
    # # options.add_argument("--headless=new")
    # # options.add_argument("--window-size=1920,1200")
    # options.add_experimental_option("detach", True)
    # # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36")
    # driver = webdriver.Chrome(options=options)#, executable_path=DRIVER_PATH)
    # driver.implicitly_wait(5)

    # Articles = []
    # articles_clicked = []

    # while True:
    #     driver.get("https://www.wiwo.de/")
    #     time.sleep(3)

    #     elements = driver.find_elements(By.CSS_SELECTOR,"[class*=js-headline]")

    #     print("Number of articles on page: {}".format(len(elements)))

    #     if len(elements) == len(articles_clicked):
    #         break        

    #     for e in elements:
    #         text_content = e.get_attribute("textContent")
    #         if text_content in articles_clicked:
    #             continue
    #         # print(e.get_attribute('class'))
    #         # print(e.get_attribute("textContent"))
    #         title = e.get_attribute("textContent")
    #         articles_clicked.append(e.get_attribute("textContent"))
    #         # print(e.text)
    #         # print(e.get_attribute("href"))
    #         # open each one
    #         # e.click()
    #         driver.execute_script('arguments[0].click()', e)
    #         time.sleep(2)
    #         try:
                # potential_titles = driver.find_element(By.CSS_SELECTOR,"[class*=c-headline]").get_attribute('textContent')
    #             title = driver.find_element(By.CSS_SELECTOR,"[class*=c-headline]").get_attribute('textContent')
    #             # title = potential_titles[0].get_attribute('textContent')
    #             # print("title {}".format(title))
    #             # for eeeee in eee:
    #             #     print(eeeee.get_attribute('class'))
    #             #     print(eeeee.get_attribute("textContent"))
    #             # print("leadtext")
    #             potential_leadtexts = driver.find_elements(By.CSS_SELECTOR,"[class*=c-leadtext]")
    #             leadtext = potential_leadtexts[0].get_attribute('textContent')
    #             # print("leadtext {}".format(leadtext))
    #             # for eeeee in eee:
    #             #     print(eeeee.get_attribute('class'))
    #             #     print(eeeee.get_attribute("textContent"))
    #             # print("category")
    #             potential_categories = driver.find_elements(By.CSS_SELECTOR,"[class*=c-overline]")
    #             category = potential_categories[0].get_attribute('textContent')
    #             title = title.replace(category,'')
    #             # for eeeee in eee:
    #             #     print(eeeee.get_attribute('class'))
    #             #     print(eeeee.get_attribute("textContent"))
            
                
                
    #             link = driver.current_url
    #             thisArticle = Article(category,title,leadtext,link)
    #             Articles.append(thisArticle)
    #             custom_print_articles(Articles)
    #         except Exception as e:
    #             print(e)
    #             pass
    #         break
    # return Articles

if __name__ == "__main__":
    scrape_wiwo()