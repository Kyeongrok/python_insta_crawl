# 쿠팡 쇼핑몰에서 1~17페이지까지 모든 상품의 url을 수집해서 .json으로 저장해보세요.

from libs.crawler import crawl
from bs4 import BeautifulSoup

def getUrl(li):
    aTag = li.find("a")
    return "https://www.coupang.com/{}".format(aTag["href"])

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    urls = [getUrl(li) for li in lis]
    return urls

def getPageUrls(pageNo):
    url = "https://www.coupang.com/np/categories/194690?page={}".format(pageNo)
    pageString = crawl(url)
    urls = parse(pageString)
    return urls

result = []
for pageNo in range(1, 17+1):
    urls = getPageUrls(pageNo)
    result = result + urls
print(len(result))

