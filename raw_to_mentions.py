import json
import JSONStreamWriter.JSONStreamWriter as JSONStreamWriter

inFile = "RC_2017-07"
outFile = "./data/mentions_july.json"
with open(inFile, 'r') as f:
    with JSONStreamWriter.ArrayWriter(outFile) as jstream:
        lineCount = 0

        for line in f:

            lineJson = json.loads(line)

            if lineJson['body'].find('u/WaterGuy12') != -1:
                jstream.write(lineJson)

            lineCount += 1

            if lineCount % 1000000 == 0:
                print('At line', lineCount)
