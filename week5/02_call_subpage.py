import json
from libs.crawler import crawl
from bs4 import BeautifulSoup

file = open("urls.json")
urlsString = file.read()

urls = json.loads(urlsString)
print(len(urls))



productInfos = []
for num in range(0, len(urls)):
    print(num)
    pageString = crawl(urls[num])
    file = open("./pages/{}.html".format(num), "w+")
    file.write(str(pageString))
    file.close()

    # productInfo = parseSubPage(pageString)
    # print(productInfo)
    # productInfos.append(productInfo)

# print(len(productInfos))
