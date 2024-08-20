from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
try:
    from webscraping.dataclass_article import Article, custom_print_articles
    import webscraping.date_parser as date_parser
except:
    from dataclass_article import Article, custom_print_articles
    import date_parser as date_parser
import datetime
import statistics

DEBUG = False
VERBOSE = False

WAITING_TIMES = 0
NUMBER_OF_ARTICLES_REPETITIONS = 5
if DEBUG:
    NUMBER_OF_ARTICLES_REPETITIONS = 2
TOLERANCE_NUMBER_ARTICLES = 3
LIMIT_ARTICLES_SCRAPE = 0.75 # percentage of articles to be scraped on website (upper bound AND successfully)


def remove_std_elements(list_number,stds = 1):
    # Calculate mean and standard deviation
    mean = statistics.mean(list_number)
    std_dev = statistics.stdev(list_number)

    # Define a function to filter elements within x standard deviation
    def filter_within_one_sigma(value):
        return mean - stds*std_dev <= value #<= mean + stds*std_dev
    # Use the filter function to create a new list
    filtered_data = list(filter(filter_within_one_sigma, list_number))

    return filtered_data


def estimate_number_of_articles(driver,website_link,article_tag):
    numbers_of_articles = []
    for _ in range(NUMBER_OF_ARTICLES_REPETITIONS):
        driver.get(website_link)
        time.sleep(WAITING_TIMES+1)
        elements = driver.find_elements(By.CSS_SELECTOR,article_tag)
        if len(elements) < 5:
            continue
        numbers_of_articles.append(len(elements))
        # print(len(elements))
        # print(elements)
    try:
        numbers_of_articles = remove_std_elements(numbers_of_articles)
    except:
        print("Except error in removing number of elements based on std for {}. \n got {} as element counts ".format(website_link,numbers_of_articles))
        if len(numbers_of_articles) == 1:
            pass
        else:
            # if len(numbers_of_articles < 1) -> wenns mehr als 1 wären, wären wir nicht in dem fehler gelandet
            numbers_of_articles = [0] # ignore website
    print("{} has {} elements".format(website_link,int(statistics.mean(numbers_of_articles))))
    return int(statistics.mean(numbers_of_articles))
        

def strip_strings(kicker,title,lead):
    return kicker.strip(),title.strip(),lead.strip()

def setup_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1200")
    # options.add_experimental_option("detach", True)

    driver:webdriver.Chrome = webdriver.Chrome(options=options)#, executable_path=DRIVER_PATH)
    driver.implicitly_wait(4)
    # driver.manage().timeouts().pageLoadTimeout(30, 45)
    # driver.manage().timeouts().implicitlyWait(30, 45) # 45 seconds, weiß nicht was die 30 bedeutet

    return driver

def extract_article_information(driver,website_element,Articles,forbidden_sites,category_tag,title_tag,leadtext_tag,date_tag,source_name):

    driver.execute_script('arguments[0].click()', website_element)
    if source_name == "NZZ" or source_name=="Handelsblatt":
        time.sleep(WAITING_TIMES+2)
    else:
        time.sleep(WAITING_TIMES)
    # time.sleep(5)
    if VERBOSE:
        print("On: {}".format(driver.current_url))
    if driver.current_url in forbidden_sites:
        # print("skip, forbidden site")
        return Articles
    error = False
    try:
        kicker = driver.find_element(By.CSS_SELECTOR,category_tag).get_attribute("textContent")
        if VERBOSE:
            print("Kicker: ",kicker)
    except:
        error = True
        if DEBUG:
            print("Kicker Element wurde nicht gefunden")
        return Articles
    try:
        title = driver.find_element(By.CSS_SELECTOR,title_tag).get_attribute("textContent")
        if source_name == "WirtschaftsWoche":
            title = title.replace(kicker,"").strip()
    except:
        error = True
        if DEBUG:
            print("Title Element wurde nicht gefunden")
        return Articles
    try:
        leadtext = driver.find_element(By.CSS_SELECTOR,leadtext_tag).get_attribute("textContent")
    except:
        error = True
        if DEBUG:
            print("Leadtext nicht gefunden")
        return Articles
    try:
        date = driver.find_element(By.CSS_SELECTOR,date_tag).get_attribute("textContent")
        if DEBUG:
            print(date)
        date = date_parser.parse_date(date.strip(),source_name)
    except Exception as e:
        error = True
        if DEBUG:
            print("Date nicht gefunden oder processing fehlgeschlagen")
            print(e)
        return Articles
    if not error:
        kicker,title,leadtext = strip_strings(kicker,title,leadtext)
        link = driver.current_url
        thisArticle = Article(kicker, title, leadtext, link, date, source_name, None)
        Articles.append(thisArticle)
    else:
        print(f"Error bei {link}")
    return Articles


def find_articles_on_website(driver,estimated_number_of_articles,website_link,article_tag):
    elements = []
    while len(elements) < estimated_number_of_articles - TOLERANCE_NUMBER_ARTICLES:
        driver.get(website_link)
        time.sleep(WAITING_TIMES+1)
        elements = driver.find_elements(By.CSS_SELECTOR,article_tag)
        if VERBOSE:
            print("Number of articles on page: {}".format(len(elements))) 

    return elements

def scrape_template(website_link, article_tag, category_tag, title_tag, leadtext_tag, date_tag,source_name,forbidden_sites = [],custom_limit = 1000, skip_first = 0):
    driver = setup_driver()
    Articles = []
    articles_clicked = []
    articles_scraped = 0
    estimated_number_of_articles = estimate_number_of_articles(driver,website_link,article_tag)

    max_number_articles_scapred = LIMIT_ARTICLES_SCRAPE * estimated_number_of_articles
    # if custom_limit != 1000:
    max_number_articles_scapred = min(custom_limit,max_number_articles_scapred)
    while articles_scraped < max_number_articles_scapred:
        elements = find_articles_on_website(driver,estimated_number_of_articles,website_link,article_tag)
        if len(elements) == len(articles_clicked):
            break
        
        number_of_elements_already_viewed = 0
        for e in elements:
            which_attribute = "textContent"
            if e.get_attribute(which_attribute) == "":
                which_attribute = "href"
            element_identifier = e.get_attribute(which_attribute)
            if DEBUG:
                print("Element identifier: {}".format(element_identifier))
            if element_identifier in articles_clicked:
                # print("continue {}".format(element_identifier))
                number_of_elements_already_viewed += 1
                if number_of_elements_already_viewed == len(elements):
                    print("Return articles as number_of_elements viewed equals total number of elements on website")
                    return Articles
                if DEBUG:
                    print("aleady seen, skipped")
                continue
            articles_clicked.append(element_identifier)
            if number_of_elements_already_viewed < skip_first:
                continue
            if VERBOSE:
                print("Scraping {} element Nr. {} of {}.\
                    \nNumber of Elements successfully scraped: {}. Scraped in total: {} (will finish at {} at the latest)".format(source_name,
                                                                                                            number_of_elements_already_viewed,
                                                                                                            estimated_number_of_articles,
                                                                                                            len(Articles),
                                                                                                            articles_scraped,
                                                                                                            int(max_number_articles_scapred))
                                                                                                                )
            articles_scraped += 1
            
            if DEBUG:
                print("Extract article information")
                print(e)
            Articles = extract_article_information(driver,e,Articles,forbidden_sites,category_tag,title_tag,leadtext_tag,date_tag,source_name)
            if VERBOSE:
                print("Scraped so far:")
                custom_print_articles(Articles)
            # break essential weil seite neu geladen werden muss um durch Elemente zu iterieren
            break

    print("{}: Return articles as limit of articles to be scraped was reached ({})".format(source_name,int(max_number_articles_scapred)))
    return Articles