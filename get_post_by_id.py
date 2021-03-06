import json
import requests
from random import randint

inFile = "./data/mentions_july.json"

with open(inFile) as data_file:
    data = json.load(data_file)

linksById = {}

for comment in data:

    postId = comment['link_id']

    if postId not in linksById:

        url = 'https://www.reddit.com/by_id/' + postId + '.json'
        headers = {'user-agent': 'teju-reddit-api-accessing' + str(randint(0, 1000))}
        r = requests.get(url=url, headers=headers)

        if r.status_code == 200:
            print(postId)
            linksById[postId] = r.json()['data']['children'][0]['data']
        else:
            print("Failure for comment ", comment)

outFile = "./data/parent_posts_july.json"
with open(outFile, 'w') as f:
    f.write('[')

    items = []
    for item in linksById.values():
        items.append(item)

    for i in range(len(items)):
        item = items[i]
        json.dump(item, f)

        if i < len(items) - 1:
            f.write(',')

    f.write(']')
