import os 
import json

data = json.load(open('./locations.json'))

for source in data["source"]:
    for file in os.listdir(source):
        extention = os.path.splitext(file)[1]

        try:
            type = data["type"][extention]
            destination = data["destination"][type]
        except:
            continue

        frm = source + '/' + file
        to = destination + '/' + file
        try:
            os.rename(frm, to)
        except:
            continue