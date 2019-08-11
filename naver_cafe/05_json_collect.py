import json

keywordList = [
    "락토핏",
    "엘레나",
    "프로스랩",
    "아임비오",
    "자로우펨도피러스",
    "셀티아이",
    "여에스더",
    "애터미",
    "암웨이",
    "레이디스밸런스",
    "듀오락",
    "닥터아돌",
    "락피도",
    "드시모네"
]

cafeIdList = [
    {"cafeName":"remonterrace", "style":"new"},
    {"cafeName":"imsanbu", "style":"new"},
    {"cafeName":"dochithink", "style":"new"},
    {"cafeName":"isajime", "style":"new"}, # 4
]

result = []
for cafeInfo in cafeIdList:
    for keyword in keywordList:
        file = open("./count_result/{}/{}.json".format(cafeInfo['cafeName'], keyword))
        ee = json.loads(file.read())
        result += ee

file = open("./result.json", "w+")
file.write(json.dumps(result))



