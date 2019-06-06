from libs.crawler import crawl
from bs4 import BeautifulSoup
from libs.patternMatcher import findMatchedTexts

url = "http://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm=%EC%85%80%ED%8A%B8%EB%A6%AC%EC%98%A8&_=1559387008602"
pageString = crawl(url)

bsObj = BeautifulSoup(pageString, "html.parser")

# 텍스트, 정규식 -> []
# findMatchedTexts(bsObj.text, "셀트리온[가-힣0-9a-zA-Z]*")
# ["셀트리온", "셀트리온스킨큐어", ---, "셀트리온~~~"]

names = findMatchedTexts(bsObj.text, "셀트리온[가-힣0-9a-zA-Z]*")

print(names)

for name in names:
    print(name)