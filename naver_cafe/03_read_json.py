import json
file = open("./01_remonterrace.json")
for item in json.loads(file.read()):
    print(item)
