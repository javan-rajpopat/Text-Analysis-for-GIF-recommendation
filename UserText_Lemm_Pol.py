import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob

def sentiment_textblob(feedback): 
        senti = TextBlob(feedback) 
        polarity = senti.sentiment.polarity 
        if -1 <= polarity < -0.5: 
                label = 'very bad' 
        elif -0.5 <= polarity < -0.1: 
                label = 'bad' 
        elif -0.1 <= polarity < 0.1: 
                label = 'ok' 
        elif 0.1 <= polarity < 0.5: 
                label = 'good' 
        elif 0.5 <= polarity <= 1: 
                label = 'positive' 
        return (polarity, label) 

str_input = input("User Text Message: ")
sentiment = sentiment_textblob(str_input)
print(sentiment)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

text = ""
for char in str_input:
   if char not in punctuations:
       text = text + char.lower()

stop_words=(set(stopwords.words("english"))  - set(["up"])).union(set(["I"]))
tokenized_word=word_tokenize(text)

filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)

lem = WordNetLemmatizer()

print("Tokenized Sentence:",tokenized_word)
print("Filtered Sentence:",filtered_sent)

lemm_sent = []
for word in filtered_sent:
    lemm_sent.append(lem.lemmatize(word,"v"))

print("Lemmatized Sentence:",lemm_sent)

