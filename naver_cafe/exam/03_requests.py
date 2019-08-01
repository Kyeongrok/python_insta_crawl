from libs.crawler import crawl
from bs4 import BeautifulSoup
url = "https://cafe.naver.com/joonggonara?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=10050146%26search.searchBy=0%26search.query=%B0%A8%B1%E2"

pageString = crawl(url)
bsObj = BeautifulSoup(pageString, "html.parser")

print(bsObj)