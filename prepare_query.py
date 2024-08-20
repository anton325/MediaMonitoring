import webscraping.dataclass_article
from typing import List
import pathlib
import pickle
import os
import datetime
import webscraping.dataclass_article as dataclass_article

today = datetime.datetime.now()
month = today.month
if month < 10:
    month = '0'+str(month)
day = today.day
if day < 10:
    day = '0' + str(day)
year = today.year - 2000
DATE_STRING = "{}{}{}".format(year,month,day)
SUBFOLDER_NAME = "Messages"+DATE_STRING
new_folder_name = "briefing{}".format(DATE_STRING)
path = pathlib.Path("Messages",SUBFOLDER_NAME)
if not os.path.exists(path):
    os.makedirs(path)

def load_added_articles():
    path = pathlib.Path("Messages", SUBFOLDER_NAME,"append.pkl")
    with open(path,"rb") as f:
        articles = pickle.load(f)
    return articles


def temp_save_articles(Articles:List[dataclass_article.Article],source):
    if len(Articles) == 0:
        print("No articles to be saved, save anyway")
        # return
    path = pathlib.Path("temp/temp_{}".format(DATE_STRING))
    if not path.exists():
        os.mkdir(path)
    # source = Articles[0].Source_name
    with open(pathlib.Path(path,"temp_{}.pkl".format(source)),"wb") as f:
        pickle.dump(Articles,f)
    
def load_temp_pickles():
    Articles:List[dataclass_article.Article] = []
    path = pathlib.Path("temp/temp_{}".format(DATE_STRING))
    for file in os.listdir(path):
        if file.split(".")[-1] != "pkl":
            continue
        with open(pathlib.Path(path,file),"rb") as f:
            loaded_articles = pickle.load(f)
            Articles.extend(loaded_articles)
    return Articles

def load_temp(path):
    pass

def check_if_temp_exists(source):
    path_to_temp_pickle = pathlib.Path("temp","temp_{}".format(DATE_STRING),"temp_{}.pkl".format(source))
    if path_to_temp_pickle.exists():
        with open(path_to_temp_pickle,"rb") as f:
            return pickle.load(f)
    else:
        return None


def remove_duplicate_articles(Articles:List[dataclass_article.Article]):
    no_duplicates = []
    for a in Articles:
        if a not in no_duplicates:
            no_duplicates.append(a)
    return no_duplicates

def load_answer():
    with open(pathlib.Path("Messages",SUBFOLDER_NAME,"answer.txt"),"r") as f:
            answer = f.read()
            return answer
        

def create_briefing_folder():
    new_folder_name = "briefing{}".format(DATE_STRING)
    path = pathlib.Path("Briefings",new_folder_name)
    if not os.path.exists(path):
        os.makedirs(path)

def create_translation_checkpoint(Articles:List[dataclass_article.Article]):
    with open(pathlib.Path("Messages",SUBFOLDER_NAME,"Articles_translated.pkl"),'wb') as f:
        pickle.dump(Articles,f)

def load_translation_checkpoint():
    with open(pathlib.Path("Messages",SUBFOLDER_NAME,"Articles_translated.pkl"),'rb') as f:
        Articles = pickle.load(f)
    return Articles

def prepare_query(Articles:List[dataclass_article.Article]):
    introduction = ""
    with open(pathlib.Path("Messages","introduction.txt")) as f:
        introduction = f.read()
    
    articles_to_be_judged = "\nJetzt kommen die Überschriften, die du selektieren sollst:\n\n"
    for article in Articles:
        articles_to_be_judged += article.Category+": "+article.Title + "\n\n"
    
    with open(pathlib.Path("Messages",SUBFOLDER_NAME,"query.txt"),"w") as f:
        f.write(introduction+"\n"+articles_to_be_judged)

    return introduction,articles_to_be_judged

def create_checkpoint(Articles:List[dataclass_article.Article], state = None):
    if state is None:
        file_name = pathlib.Path("Messages",SUBFOLDER_NAME,"Articles.pkl")
    else:
        file_name = pathlib.Path("Messages",SUBFOLDER_NAME,f"Articles_{state}.pkl")
    with open(file_name,'wb') as f:
        pickle.dump(Articles,f)

def load_checkpoint(state = None):
    if state is None:
        articles_path = pathlib.Path("Messages",SUBFOLDER_NAME,"Articles.pkl")
    else:
        articles_path = pathlib.Path("Messages",SUBFOLDER_NAME,f"Articles_{state}.pkl")
        
    with open(articles_path,'rb') as f:
        Articles = pickle.load(f)
    with open(pathlib.Path("Messages","introduction.txt"),"r") as f:
        introduction = f.read()
    articles_to_be_judged = "\nJetzt kommen die Überschriften, die du selektieren sollst:\n\n"
    for article in Articles:
        articles_to_be_judged += article.Category+": "+article.Title + "\n\n"
    return introduction,articles_to_be_judged,Articles
    

def save_answer(answer:str):
    with open(pathlib.Path("Messages",SUBFOLDER_NAME,"answer.txt"),"w") as f:
        f.write(answer)

def load_introduction():
    with open(pathlib.Path("Messages","introduction.txt"),"r") as f:
        return f.read()
    
def load_example_articles():
    with open(pathlib.Path("Messages","examples.txt"),"r") as f:
        return f.read()
    
def export_unclassified_articles(articles_not_found:List[dataclass_article.Article]):
    message = "Diese Artikel konnten nicht zugeordnet werden:\n"
    for a in articles_not_found:
        message += "\n"+a

    with open(pathlib.Path("Messages",SUBFOLDER_NAME,"not_found_articles.txt"),"w") as f:
        f.write(message)

def export_selected_articles(Articles:List[dataclass_article.Article]):
    message = "ChatGPT schlägt vor folgende Artikel auszuwählen:\n"
    for a in Articles:
        message += "\n"+a.Category + ": " + a.Title + "\nFound at: "+a.Link

    with open(pathlib.Path("Messages",SUBFOLDER_NAME,"selected_articles.txt"),"w") as f:
        f.write(message)

