# dart에서 추가로 로딩되는 데이터의 주소에 http request를
# 보내서 오는 데이터를 console에 출력 해보세요.
import requests
import re
from bs4 import BeautifulSoup

def crawl(url):
    res = requests.get(url)
    return res.content
url = "http://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm=현대"
pageString = crawl(url)
bsobj = BeautifulSoup(pageString, "html.parser")
string = str(bsobj)

matched = re.findall("..경매[가-힣A-Z]*", string)
# print(string)
for keyword in matched:
    print(keyword)