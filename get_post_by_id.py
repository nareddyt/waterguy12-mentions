import json
import requests
from random import randint

inFile = "./data/mentions_july.json"

with open(inFile) as data_file:
    data = json.load(data_file)

linksById = {}

count = 0
for comment in data:

    if count > 2:
        break

    postId = comment['link_id']

    if postId not in linksById:

        count += 1

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
    myList = ','.join(map(str, linksById.values()))
    json.dump(myList, f)
    f.write(']')
