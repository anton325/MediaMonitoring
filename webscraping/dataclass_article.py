from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    Category: str
    Title: str
    Leadtext: str
    Link: str
    Date: datetime
    #Text: str
    Source_name: str
    tier_one: str

    def __eq__(self, other):
        # Define the custom equality comparison logic
        return self.Link == other.Link


def custom_print_articles(articles):
    print("All articles found so far:")
    for a in articles:
        custom_print_article(a)
        print("\n")


def custom_print_article(article):
    message = "{}: {} {} Found at {} on {}".format(article.Category,article.Title,article.Leadtext,article.Link,article.Date)
    if article.tier_one is not None:
        message += f"Tier one: {article.tier_one}"
    print(message)


def custom_print_articles_short(articles):
    print("All articles found so far:")
    for a in articles:
        custom_print_article_short(a)
        print("\n")

def custom_print_article_short(article):
    print("{}: {}".format(article.Category,article.Title))