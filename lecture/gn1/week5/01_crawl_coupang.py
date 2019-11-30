from libs.crawler import crawl
from bs4 import BeautifulSoup

def getUrl(li):
    aTag = li.find("a")
    link = aTag["href"]
    return "https://www.coupang.com" + link

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    productList = bsObj.find("ul", {"id":"productList"})
    lis = productList.findAll("li")

    urls = [ getUrl(li) for li in lis]
    return urls

def getSubPageUrls(pageNum):
    url = "https://www.coupang.com/np/categories/186764?page={}".format(pageNum)
    pageString = crawl(url)
    subPageUrls = parse(pageString)
    return subPageUrls

allSubUrls = []
for num in range(1, 17+1):
    allSubUrls = allSubUrls + getSubPageUrls(num)

import json
file = open("urls.json", "w+")
file.write(json.dumps(allSubUrls))
# print(len(allSubUrls))
