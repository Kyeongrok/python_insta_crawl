from libs.crawler import crawl
from bs4 import BeautifulSoup

url = "http://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm=셀트리&_=1558022515791"

pageString = crawl(url)
bsObj = BeautifulSoup(pageString, "html.parser")
print(bsObj)