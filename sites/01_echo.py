import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content


def getPrductInfo(tr):
    tds = tr.findAll("td")
    return {"no": tds[0].text, "name": tds[1].text, "category": tds[2].text,
            "vendor": tds[3].text, "confirmNo": tds[4].text, "licenseNo": tds[5].text}


def parser(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    table = bsObj.find("table", {"class": "table table-striped2"})
    tbody = table.find("tbody")

    trs = tbody.findAll("tr")

    productInfos = []
    for tr in trs:
        productInfo = getPrductInfo(tr)
        productInfos.append(productInfo)

    return productInfos


def crawlPage(pageNo):
    url = "http://ecolife.me.go.kr/ecolife/sntryAid/index?page={}".format(pageNo)
    pageString = crawl(url)
    products = parser(pageString)
    return products


def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()


result = []
for pageNo in range(1, 164 + 1):
    infos = crawlPage(pageNo)
    print(infos)
    time.sleep(1)
    # result = result

# print(result)
# print(len(result))
#
# df = pd.DataFrame(data=result)
# print(df.count())
# save(df, "./ecolife.xlsx")
