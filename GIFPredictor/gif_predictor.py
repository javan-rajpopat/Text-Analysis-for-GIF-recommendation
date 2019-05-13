from __future__ import unicode_literals
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from nltk.corpus import stopwords
from collections import OrderedDict
from operator import itemgetter
import spacy
import numpy
import csv
import json
import math

# Libraries for data pre-processing
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
from nltk.corpus import wordnet

nlp = spacy.load('en_core_web_lg')
doc2 = []
with open('data_gifs_newest4.json') as json_file:
    json_reader = json.load(json_file)
    for row in json_reader:
        doc2.append(row)


# function to sort JSON object based on score attribute
def extract_time(json):
    try:
        return int(json['Score'])
    except KeyError:
        return 0


# function gets executed only once, model is trained using this function
def model_trainer():
    # load model, english, used for doc2vec
    doc = []
    id_keeper = {}
    with open('data_gifs3.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            doc.append(row[2])
            id_keeper.update({row[2]: row[0]})

    # vectorizing each words in the dataset using Tfid
    documents = doc
    vectorizer = TfidfVectorizer(
        stop_words=(set(stopwords.words("english")) - set(["up"])).union(set(["I"]), set(["gif"]), set(["na"])))
    X = vectorizer.fit_transform(documents)

    # model gets trained here
    true_k = 6000
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=10, n_init=1)
    model.fit(X)
    print("in",model.inertia_)


    # Helps to know the tags in each cluster
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()

    for i in range(true_k):
        print("Cluster %d:" % i),
        for ind in order_centroids[i, :5]:
            print(' %s' % terms[ind]),
        print
    return model, doc, order_centroids, terms


def cluster_analysis(model, str_input, doc, order_centroids, terms):
    # Define the puncuations marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    print("in", model.inertia_)
    # remove punctuations and convert to lower case
    text = ""
    for char in str_input:
        if char not in punctuations:
            text = text + char.lower()

    # removing stopwords
    stop_words = (set(stopwords.words("english")))
    tokenized_word = word_tokenize(text)

    # word tokenizing
    filtered_sent = []
    for w in tokenized_word:
        if w not in stop_words:
            filtered_sent.append(w)

    lem = WordNetLemmatizer()

    # Lemmatized sentence by user
    lemm_sent = []
    for word in filtered_sent:
        lemm_sent.append(lem.lemmatize(word, "v"))

    lemm__sent = ""
    for l in lemm_sent:
        lemm__sent += " " + str(l)
    print(lemm__sent)

    # Predicting the cluster of the input
    print("\n")
    print("Prediction")
    user_input = str(lemm_sent)

    documents = doc
    vectorizer = TfidfVectorizer(
        stop_words=(set(stopwords.words("english")) - set(["up"])).union(set(["I"]), set(["gif"]), set(["na"])))
    X = vectorizer.fit_transform(documents)

    Y = vectorizer.transform([user_input])
    prediction = model.predict(Y)
    print(prediction)

    # Remove the tags in the related clusters
    tags = []
    for ind in order_centroids[prediction[0], :5]:
        tags.append(terms[ind])

    relevent_tuples = []
    for d in doc2:
        if d['Tag'] in tags:
            relevent_tuples.append(d)
    print(tags)

    doc1 = nlp(u'' + user_input)
    print(doc1)
    output = {}
    for each in relevent_tuples:
        output.update({each['id']: [doc1.similarity(nlp(each['description'])), 0]})

    # Output final results
    output = OrderedDict(sorted(output.items(), key=itemgetter(1), reverse=True))
    print(len(output.keys()))

    weight_score = 0.3
    weight_simmilarity = 0.7

    temp = []
    for i in doc2:
        if i["id"] in output.keys():
            i["temp_score"] = (weight_score * i["Score"]) + (weight_simmilarity * output[i["id"]][0])
            temp.append(i)

    # Quick sort to arrange GIFs in descending order of Scores

    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]["Score"]
        for j in range(low, high):
            if arr[j]["Score"] >= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quickSort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)

    quickSort(temp, 0, 1)  # Calling QuickSor

    # HyperParameters set by us, not sure on the values yet
    T = 0.18

    # Paramater taken from user, for how many option he/she wants
    n = 10  # Assuming he picks 10
    r = round(n / 10)  # Keeping 1/10th of randomness in the algorithm, reason explained in PDF

    # All gifs that will be displayed to user
    output_final = []
    output_final_ids = []

    # Keep a track of their index values
    print("temp here")

    temp.sort(key=extract_time, reverse=True)
    print(temp)
    for g in range(len(temp)):  # Clearing Threshold
        output_final.append(temp[g])
        output_final_ids.append(temp[g]['id'])
    count = 0
    executed = 0

    # Creating random GIFs to display (Reason in pdf)
    while count < r and executed < 100:
        executed += 1
        c = int(numpy.random.uniform(0, len(temp)))
        if c not in output_final_ids:
            output_final.append(temp[c])
            output_final_ids.append(temp[c]['id'])
            count += 1
    print(len(output.keys()))
    return output_final, T, output_final_ids


def score_manipulator(output, selected_gif, output_final_ids, T):
    Gif_selected_id = selected_gif
    alpha = 2
    beta = 0.05
    output_final_ids = output_final_ids.replace('[', '').replace(']', '').split(',')
    for i in range(len(output_final_ids)):
        output_final_ids[i] = int(output_final_ids[i])
    for o in doc2:
        if o['id'] == int(Gif_selected_id):
            o['Score'] = o['Score'] + 1
        elif o['id'] in output_final_ids and o['id'] != int(Gif_selected_id):
            o['Score'] = o['Score'] - 1
    with open('data_gifs_newest4.json', 'w') as outfile:
        json.dump(doc2, outfile)
