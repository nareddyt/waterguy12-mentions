import json
import JSONStreamWriter.JSONStreamWriter as JSONStreamWriter

filename = "RC_2017-07"
outFile = "./mentions.json"
with open(filename, 'r') as f:
    with JSONStreamWriter.ArrayWriter(outFile) as jstream:
        lineCount = 0

        for line in f:

            lineJson = json.loads(line)

            if lineJson['body'].find('u/WaterGuy12') != -1:
                jstream.write(lineJson)

            lineCount += 1

            if lineCount % 1000000 == 0:
                print('At line', lineCount)
