    
import nltk
import json

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob

# Function to find polarity
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
        pol = float(polarity)
        return (pol)

with open('tgif-v1.0.json', 'r+') as json_data: 
    data = json.load(json_data)
    for x in data:
        str_input = x['description']
        x['Sentiment'] = sentiment_textblob(str_input)
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        text = ""
        for char in str_input:
            if char not in punctuations:
                text = text + char.lower()
        stop_words=(set(stopwords.words("english"))  - set(["up"])).union(set(["I"]),set(["gif"]))
        tokenized_word=word_tokenize(text)
        filtered_sent=[]
        for w in tokenized_word:
            if w not in stop_words:
                filtered_sent.append(w)
        lem = WordNetLemmatizer()
        lemm_sent = []
        for word in filtered_sent:
            lemm_sent.append(lem.lemmatize(word,"v"))
        x['description'] = str(lemm_sent)
        
with open('tgif-v1.0_clean.json', 'w') as data_file:
    data = json.dump(data, data_file)