import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
#from nltk import ngrams

str_input = input("User Text Message: ")
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

print(text)
print("Tokenized Sentence:",tokenized_word)
print("Filterd Sentence:",filtered_sent)

lemm_sent = []
for word in filtered_sent:
    lemm_sent.append(lem.lemmatize(word,"v"))

#grams = ngrams(lemm_sent, 3)

#for gr in grams:
#    print (gr)

print("Lemmatized Sentence:",lemm_sent)