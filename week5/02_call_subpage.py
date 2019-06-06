import json
from libs.crawler import crawl
from bs4 import BeautifulSoup

file = open("urls.json")
urlsString = file.read()

urls = json.loads(urlsString)
print(len(urls))

productInfos = []
for num in range(0, len(urls)):
    url = urls[num]
    print(url)
    pageString = crawl(url)
    file = open("./pages/{}.html".format(num), "w+", encoding="utf-8")
    file.write(str(pageString.decode("utf-8")))
    file.close()

    # productInfo = parseSubPage(pageString)
    # print(productInfo)
    # productInfos.append(productInfo)

# print(len(productInfos))
