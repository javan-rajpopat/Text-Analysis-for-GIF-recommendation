import nltk
import csv

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet


# added for future tasks
# import difflib
# import keyword
# from nltk.stem import PorterStemmer
# from nltk import ngrams

def gifGetter(input_text):
    # removing stop words with custom dictionary
    punctuations = '''!()-[]{};:'"\,'<>./?@#$%^&*_~'''
    stop_words = set(stopwords.words('english') + ['The', 'This', 'that', 'the', 'these', 'those', 'That', 'that'])

    # random text input taken from the user
    text_input = input_text

    # Converting input into tokens
    word_tokens = word_tokenize(text_input)
    filtered_sentence = [w for w in word_tokens if not w in stop_words and not w in punctuations]

    # lemmatizing each word of input text
    lemm = WordNetLemmatizer()
    search_on = []

    for i in filtered_sentence:
        search_on.append(lemm.lemmatize(i))

    # finding all possible synonyms of each lemmatized words
    synonym_dict = []

    for word in search_on:
        for syn in wordnet.synsets(word):
            nxt = []
            for l in syn.lemmas():
                nxt.append(l.name())
            if word not in nxt:
                nxt.append(word)
        synonym_dict.append(nxt)

    # reading our data-set
    gif_ids = []
    gif_labels = []
    gif_links = []

    result_dict = {}
    final_gif = []

    with open('giphy.csv', 'rt') as csvfile:

        gifreader = csv.reader(csvfile, delimiter=',')
        next(gifreader)
        for row in gifreader:
            gif_ids += [row[0]]
            gif_labels += [row[4]]
            gif_links += [row[1]]

        for label, iterator in zip(gif_labels, range(0, len(gif_ids))):
            word_tokens = word_tokenize(label)
            filtered_sentence = [w for w in word_tokens if not w in stop_words and not w in punctuations]
            ne_tags = nltk.pos_tag(filtered_sentence)
            lemm = WordNetLemmatizer()
            search_on = []
            for i in filtered_sentence:
                search_on.append(lemm.lemmatize(i, pos="a"))
            result_dict.update({gif_ids[iterator]: search_on})

        # returning all gif_ids who intersect with synonym dictionary of the input
        for words in synonym_dict:
            for ids, label in result_dict.items():
                if set(words).intersection(label):
                    final_gif.append(ids)

    print(final_gif)

# function to get matching gif ids based on text given
gifGetter("The US president says it is funny nodding hustling")
