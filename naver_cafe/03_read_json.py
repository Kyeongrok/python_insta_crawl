import json
file = open("./ret_gamgi.json")
for item in json.loads(file.read()):
    print(item)
