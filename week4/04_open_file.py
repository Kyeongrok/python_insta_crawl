from bs4 import BeautifulSoup

# companyinfo.html 을 불러와서 콘솔에 출력 해보세요
file = open("./companyinfo.html", encoding="utf-8")
pageString = file.read()
bsObj = BeautifulSoup(pageString, "html.parser")
tableScroll = bsObj.find("div", {"class":"table_scroll"})
tbody = tableScroll.find("tbody")

trs = tbody.findAll("tr")
def getCompanyInfo(tr):
    tds = tr.findAll("td")
    name = tds[0].text.replace("\n", "").replace("\t", "")
    chief = tds[1].text
    return {"name":name, "chief":chief, "code":tds[2].text, "businessCategory":tds[3].text}

# infos = []
# for tr in trs:
#     infos.append(getCompanyInfo(tr))

companyInfos = [ getCompanyInfo(tr) for tr in trs]

print(len(companyInfos))
print(companyInfos[0])

import json
file = open("companyInfo.json", "w+", encoding="utf-8")
file.write(json.dumps(companyInfos))

# pandas설치
# pandas에서 json을 dataframe으로 불러오기


