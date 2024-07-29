import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'https://edition.cnn.com/2024/07/28/entertainment/lady-gaga-michael-polansky-engaged/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print('Title:', article.title)
print('Authors:', article.authors)
print('Publish Date:', article.publish_date)
print('Summary:', article.summary)
