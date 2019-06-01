from libs.crawler import crawl
from bs4 import BeautifulSoup
import re
from libs.patternMatchedTextGetter import getMatchedText

url = "http://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm=%EC%85%80%ED%8A%B8%EB%A6%AC&_=1557541592603"
pageString = crawl(url)
print(pageString)
bsObj = BeautifulSoup(pageString, "html.parser")

file = open("cell.txt", "w+", encoding="utf-8")
file.write(bsObj.text)

# text를 file에서 불러오려면?
text = bsObj.text

result = getMatchedText("셀트리온.*", text)
print(result)
