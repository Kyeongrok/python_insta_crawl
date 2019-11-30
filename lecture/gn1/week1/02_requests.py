import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

url = "https://www.instagram.com/explore/tags/발레"
pageString = crawl(url)
bsObj = BeautifulSoup(pageString, "html.parser")
ul = bsObj.find("div", {"class":"Nnq7C weEfm"})
print(bsObj)