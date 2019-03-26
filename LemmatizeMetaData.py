import nltk
import json

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

with open('giphy.json', 'r+') as json_data, open('lemm_giphy.json', 'a+') as json_write:
    data = json.load(json_data)
    for x in data:
        str_input = x['GIPHY Title']
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
        x['GIPHY Title'] = lemm_sent
        json_write.seek(0)
        json_write.write(json.dumps(x))
        json_write.truncate()
