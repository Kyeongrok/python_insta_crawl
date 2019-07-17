from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import random
from bs4 import BeautifulSoup
import json
import pandas as pd

chrome_options = Options()
# chrome_options.add_argument("--headless")

rootPath = ".."
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver74".format(rootPath),
    options=chrome_options
)

def getProductInfo(tr):
    tds = tr.findAll("td")
    return {"no":tds[0].text, "name":tds[1].text, "category":tds[2].text,
            "vendor":tds[3].text, "confirmNo":tds[4].text, "licenceNo":tds[5].text
            }

def parser(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    table = bsObj.find("table", {"class":"table table-striped2"})
    tbody = table.find("tbody")

    trs = tbody.findAll("tr")

    productInfos = []
    for tr in trs:
        productInfo = getProductInfo(tr)
        productInfos.append(productInfo)

    return productInfos

url = "http://ecolife.me.go.kr/ecolife/sntryAid/index?page=6"
driver.get(url)

result = []
def getInfos(pageNo):
    url = "http://ecolife.me.go.kr/ecolife/sntryAid/index?page={}".format(pageNo)
    driver.get(url)
    pageSource = driver.page_source
    infos = parser(pageSource)
    return infos


def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

for pageNo in range(1, 164 + 1):
    result = result + getInfos(pageNo)

df = pd.DataFrame(data=result)
print(df.count())
save(df, "./ecolife.xlsx")

