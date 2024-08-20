import datetime
import pathlib
import pickle as pkl
import numpy as np
from webscraping.dataclass_article import Article, custom_print_articles
import time
from utils.get_time import get_current_date_string
import tkinter as tk
from tkinter import ttk

def save_articles(articles):
    date_string = get_current_date_string()
    with open(pathlib.Path("Messages", f"Messages{date_string}", "append.pkl"), 'wb') as f:
        pkl.dump(articles, f)
    print(f'Articles saved to {pathlib.Path("Messages", f"Messages_{date_string}", "append.pkl")}')

def convert_date_to_datetime(date):
    """
    date ist bloß sowas wie 1.10. (also dd.mm.)
    """
    date = date[:-1]
    day = int(date.split(".")[0])
    month = int(date.split(".")[1])
    year = datetime.datetime.now().year
    return datetime.datetime(year, month,day,0,0,0)


class ArticlesGUI:

    def __init__(self, master):
        self.articles = []
        self.master = master
        self.master.title("Simple GUI")
        self.master.geometry("800x500")

        # Create labels and entry widgets
        ttk.Label(master, text="Überschrift").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.uberschrift_entry = ttk.Entry(master, width=50, font=('Helvetica', 14))
        self.uberschrift_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(master, text="Quelle").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.quelle_entry = ttk.Entry(master, width=50, font=('Helvetica', 14))
        self.quelle_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(master, text="Datum (dd.mm.)").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.datum_entry = ttk.Entry(master, width=50, font=('Helvetica', 14))
        self.datum_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(master, text="Link").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.link_entry = ttk.Entry(master, width=50, font=('Helvetica', 14))
        self.link_entry.grid(row=3, column=1, padx=10, pady=5)


        ttk.Label(master, text="Text").grid(row=5, column=0, padx=10, pady=5, sticky="ne")
        self.text_entry = tk.Text(master, width=50, height=10, font=('Helvetica', 14))
        self.text_entry.grid(row=5, column=1, padx=10, pady=5)


        # Create the buttons
        self.next_button = ttk.Button(master, text="Next", command=self.next_button)
        self.next_button.grid(row=6, column=1, padx=10, pady=10, sticky="e")

        self.done_button = ttk.Button(master, text="Done", command=self.done_button)
        self.done_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    def delete_old_entries(self):
        self.uberschrift_entry.delete(0, tk.END)
        self.quelle_entry.delete(0, tk.END)
        self.datum_entry.delete(0, tk.END)
        self.link_entry.delete(0, tk.END)
        self.text_entry.delete("1.0", tk.END)

    def next_button(self):
        uberschrift_value = self.uberschrift_entry.get().strip('\n')
        quelle_value = self.quelle_entry.get().strip('\n')
        datum_value = self.datum_entry.get().strip('\n')
        link_value = self.link_entry.get().strip('\n')
        text_value = self.text_entry.get("1.0", tk.END).strip('\n')

        # Print values to console (or handle them as needed)
        print("Überschrift:", uberschrift_value)
        print("Quelle:", quelle_value)
        print("Datum:", datum_value)
        print("Link:", link_value)
        print("Text:", text_value)

        try:
            date = convert_date_to_datetime(datum_value)
        except:
            date = None
        infered_article = Article(None, uberschrift_value, text_value, link_value, date, quelle_value)
        print("Article created")

        self.articles.append(infered_article)
        custom_print_articles(self.articles)
        self.delete_old_entries()

    def done_button(self):
        print("Done button pressed")
        save_articles(self.articles)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArticlesGUI(root)
    root.mainloop()
