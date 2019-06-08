# pages/n.html을 각각 불러서 상품명, 상품평 개수
from bs4 import BeautifulSoup

def parseSubpage(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    title = bsObj.find("h2", {"class":"prod-buy-header__title"})
    count = bsObj.find("span", {"class":"count"})
    price = 0
    try:
        price = bsObj.find("span", {"class":"total-price"})
        price = price.text.strip() # 10,000원
        price = price.replace("원", "").replace(",", "")
        if(price == ""): price = 0
        print(price)
    except Exception as e:
        print("--error during parse--", title, e )

    return {"title":title.text, "count":count.text, "price":price}

productInfos = []
for index in range(0, 1020):
    try:
        print(index)
        file = open("./pages/{}.html".format(index))
        pageString = file.read()
        file.close()
        productInfo = parseSubpage(pageString)
        productInfos.append(productInfo)
    except Exception as e:
        print("--error--{}".format(index), e)

import json
print(len(productInfos))
file = open("./result.json", "w+")
file.write(json.dumps(productInfos))
