import customtkinter as ctk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

def show_article_info():
    url = url_entry.get()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.configure(text=article.title)
    authors.configure(text=', '.join(article.authors))
    publish_date.configure(text=str(article.publish_date))
    summary.insert("0.0", article.summary)


def clear():
    url_entry.delete(0, ctk.END)
    title.configure(text='')
    authors.configure(text='')
    publish_date.configure(text='')
    summary.delete("0.0", ctk.END)

root = ctk.CTk()
root.title('Article Summarizer')
root.geometry('600x600')
root.resizable(False, False)

heading = ctk.CTkLabel(root, text='Article Summarizer', font=('Verdana', 16))
heading.pack(pady=10)

url_label = ctk.CTkLabel(root, text='URL:', font=('Verdana', 14))
url_label.pack(pady=5)

url_entry = ctk.CTkEntry(root, width=600)
url_entry.pack(pady=5)

title_label = ctk.CTkLabel(root, text='Title:', font=('Verdana', 14))
title_label.pack(pady=5)

title = ctk.CTkLabel(root, text='')
title.pack(pady=5)

authors_label = ctk.CTkLabel(root, text='Authors:', font=('Verdana', 14))
authors_label.pack(pady=5)

authors = ctk.CTkLabel(root, text='')
authors.pack(pady=5)

publish_date_label = ctk.CTkLabel(root, text='Publish Date:', font=('Verdana', 14))
publish_date_label.pack(pady=5)

publish_date = ctk.CTkLabel(root, text='')
publish_date.pack(pady=5)

summary_label = ctk.CTkLabel(root, text='Summary:', font=('Verdana', 14))
summary_label.pack(pady=5)

summary = ctk.CTkTextbox(root, width=600, height=100)
summary.pack(pady=5)

show_info_button = ctk.CTkButton(root, text='Info', command=show_article_info)
show_info_button.pack(pady=5)

clear_button = ctk.CTkButton(root, text='Clear', command=clear)
clear_button.pack(pady=5)

root.mainloop()
