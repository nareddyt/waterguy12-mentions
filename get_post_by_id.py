import json
import requests
from random import randint

filename = "./mentions_july.json"

with open(filename) as data_file:
    data = json.load(data_file)

linksById = {}

for comment in data:

    postId = comment['link_id']

    if postId in linksById:

        url = 'https://www.reddit.com/by_id/' + postId + '.json'
        headers = {'user-agent': 'teju-reddit-api-accessing' + randint(0, 1000)}
        r = requests.get(url=url, headers=headers)

        if r.status_code == 200:
            linksById[postId] = r.json()
        else:
            print("Failure for comment ", comment)

linksJson = json.dumps(linksById, ensure_ascii=True)

outFile = "./parent_posts_july.json"
with open(outFile, 'w') as outfile:
    json.dump(data, outfile)