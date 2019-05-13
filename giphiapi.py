import time
import giphy_client
import json
from giphy_client.rest import ApiException
import requests
import csv
import csvreader
# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'Y5NaEc73uCCCIT07a6of2deQeYJAz0DM'  # str | Giphy API Key.
user_input = "Something is fishy"
count = 1
data = []
title_gif = []
url_gif = []
id_gif = []
tag_gif = []
category = []
category = csvreader.readfile()
try:
    for tag in category:
        new_string = tag.replace(" ", "+")


        resp = requests.get('http://api.giphy.com/v1/gifs/search?q=' + new_string + '&api_key=HlrJoPBRapwrY0ub64Q0Wk6qpxvv68cr&limit=25&images={width=320&height=200}')


        gh = resp.json()

        for i in gh['data']:
            title_gif.append(i['title'])
            tag_gif.append(tag)
            url_gif.append(i['url'])
            id_gif.append(i['id'])
            print(tag)
            url_ghs = 'https://media1.giphy.com/media/' + i['id'] + '/200_d.gif'
            # print(url_ghs)

    for id, title, url, tag in zip(id_gif, title_gif, url_gif, tag_gif):
        url_ghs = 'https://media1.giphy.com/media/' + id + '/200_d.gif'

        if not title or title == "" or title == " ":
            continue
        data.append({
            'id': count,
            'description': title,
            'link': url_ghs,
            'Score': 0.5,
            'Tag': tag
        })
        count += 1

    stack_data = json.dumps(data)
    with open('data_gifs_newest3.json', 'w') as outfile:
        json.dump(data, outfile)

    count = 0
    with open('data_gifs3.csv', mode='w') as data_gifs:
        data_gifs = csv.writer(data_gifs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url, title,id,tag in zip(url_gif, title_gif,id_gif,tag_gif):
            url_gh = 'https://media1.giphy.com/media/'+id+'/200_d.gif'
            data_gifs.writerow([count,url_gh,title,0.5,tag])
            count+=1

except ApiException as e:
    print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


