from libs.coupang.subpageParser import parse

productInfos = []
# 파일 읽기
def openAndParse(num):
    file = open("./pages/{}.html".format(num), encoding="utf-8")
    pageString = file.read()
    file.close()
    productInfo = parse(pageString)
    return productInfo

for i in range(0, 1000):
    print(i)
    productInfos.append(openAndParse(i))

print("total:", len(productInfos))

import json
file = open("./result.json", "w+")
file.write(json.dumps(productInfos))