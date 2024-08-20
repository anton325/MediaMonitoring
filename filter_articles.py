import datetime
import pathlib
import webscraping.dataclass_article as dataclass_articles
from typing import List
import pickle
import sentence_transformers 

def filter_articles_by_date(Articles:List[dataclass_articles.Article]) -> List[dataclass_articles.Article]:
    # filter append article when written in fitting timeframe
    # on mondays we can go back to saturday (2 days)
    # else only one day
    backwards_horizont = 2
    if datetime.date.today().weekday() == 0:
        backwards_horizont = 3
    jetzt = datetime.datetime.now()
    date_threshold = jetzt - datetime.timedelta(days=backwards_horizont)
    date_threshold = date_threshold.replace(hour=23,minute=59)

    filtered_articles = []
    for a in Articles:
        if a.Date > date_threshold:
            filtered_articles.append(a)

    return filtered_articles

def filter_already_seen_exact_match(Articles:List[dataclass_articles.Article]) -> List[dataclass_articles.Article]:
    # wenn Überschrift gleich, oder Link gleich (UND Quelle gleich?) dann überspringe den Artikel. Sonst füge Artikel gefilterten Liste hinzu
    filtered_articles = []
    yesterday_articles = load_yesterday_articles()
    for a_today in Articles:
        eliminate = False
        for a_yesterday in yesterday_articles:
            if a_today.Title == a_yesterday.Title:
                eliminate = True
                break
            if a_today.Link == a_yesterday.Link:
                eliminate = True
                break
        if not eliminate:
            filtered_articles.append(a_today)
    return filtered_articles

def filter_already_seen_embeddings(Articles:List[dataclass_articles.Article]) -> List[dataclass_articles.Article]:
    # compare embeddings of Kicker: Title
    model = sentence_transformers.SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    filtered_articles = []
    yesterday_articles = load_yesterday_articles()
    yesterday_articles_embeddings = {}
    for a_yesterday in yesterday_articles:
        # yesterday_articles_embeddings[a_yesterday.Link] = model.encode(a_yesterday.Category+": "+a_yesterday.Title, convert_to_tensor=True)
        yesterday_articles_embeddings[a_yesterday.Link] = model.encode(a_yesterday.Category+": "+a_yesterday.Title +" "+a_yesterday.Leadtext, convert_to_tensor=True)

    for a_today in Articles:
        # embedding_today = model.encode(a_today.Category+": "+a_today.Title, convert_to_tensor=True)
        embedding_today = model.encode(a_today.Category+": "+a_today.Title + " "+ a_today.Leadtext, convert_to_tensor=True)
        eliminate = False
        for a_yesterday in yesterday_articles:
            embedding_score = sentence_transformers.util.pytorch_cos_sim(embedding_today,yesterday_articles_embeddings[a_yesterday.Link])
            # if "Porsche" in a_yesterday.Title and "Porsche" in a_today.Title:
            #     print(a_today.Title)
            #     print(a_yesterday.Title)
            #     print(embedding_score)
            if  embedding_score > 0.75:
                # print("Filter:")
                # dataclass_articles.custom_print_article_short(a_today)
                # dataclass_articles.custom_print_article_short(a_yesterday)
                # print(sentence_transformers.util.pytorch_cos_sim(embedding_today,yesterday_articles_embeddings[a_yesterday.Link]))
                eliminate = True
                break
        if not eliminate:
            filtered_articles.append(a_today)
    return filtered_articles

def filter_same_topic_articles(Articles:List[dataclass_articles.Article]) -> List[dataclass_articles.Article]:
    order_of_sources = ['Handelsblatt','WirtschaftsWoche','Manager-Magazin','FAZ','Sueddeutsche','Tagesschau','Logistik-heute','Ingenieur.de','Produktion.de','NZZ',\
                        'Elektroniknet.de','Deutschlandfunk','Capital','Beschaffung-Aktuell','Spiegel.de','Tagesspiegel','Springer-Professional','Industry-of-things','WELT']
    articles_embeddings = {}
    filtered_articles = []
    deleted_articles = []
    model = sentence_transformers.SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    for a in Articles:
        articles_embeddings[a.Link] = model.encode(a.Category+": "+a.Title, convert_to_tensor=True)

    for a1 in Articles:
        eliminate = False
        for a2 in Articles:
            if a1.Title == a2.Title and a1.Source_name == a2.Source_name:
                continue
            if sentence_transformers.util.pytorch_cos_sim(articles_embeddings[a1.Link],articles_embeddings[a2.Link]) > 0.73:
                # print("found: ")
                # print(a1.Category,": ",a1.Title,a1.Source_name)
                # print(a2.Category,": ",a2.Title,a2.Source_name)
                eliminate = True
                if order_of_sources.index(a1.Source_name) > order_of_sources.index(a2.Source_name): # -> a2 better source than a1
                    if a2 not in filtered_articles and a2 not in deleted_articles:
                        filtered_articles.append(a2)
                        deleted_articles.append(a1)
                else:
                    if a1 not in filtered_articles and a1 not in deleted_articles:
                        filtered_articles.append(a1)
                        deleted_articles.append(a2)
                
                # Articles.remove(a1)
                # Articles.remove(a2)
                break
        
        if not eliminate:
            filtered_articles.append(a1)
    return filtered_articles




def load_yesterday_articles() -> List[dataclass_articles.Article]:
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    # wenn heute montag ist -> yesterday = friday, also 3 Tage zurück)
    if datetime.date.today().weekday() == 0:
        yesterday = datetime.datetime.now() - datetime.timedelta(days=3)
    month = yesterday.month
    if month < 10:
        month = '0'+str(month)
    day = yesterday.day
    if day < 10:
        day = '0' + str(day)
    year = yesterday.year - 2000
    SUBFOLDERSTRING = "Messages{}{}{}".format(year,month,day)
    with open(pathlib.Path("Messages",SUBFOLDERSTRING,"Articles.pkl"),'rb') as f:
        Articles_yesterday = pickle.load(f)
    return Articles_yesterday
