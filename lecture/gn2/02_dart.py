from selenium import webdriver
import time, random
from bs4 import BeautifulSoup
from libs.dartReportListParser import parse as dartReportListParse
from libs.dartReportListParser import downloadLinkParse

driver = webdriver.Chrome(
    executable_path="../../chrome/chromedriver77"
)

url = "http://dart.fss.or.kr/"
driver.get(url)

driver.find_element_by_xpath('//*[@id="textCrpNm"]').send_keys("셀트리온")
driver.find_element_by_xpath('//*[@id="btnOpenFindCrp"]').click()

time.sleep(2)

driver.find_element_by_xpath('/html/body/div[13]/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[1]/table/tbody/tr[2]/td[1]/div/input[1]').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="corpListContents"]/div/fieldset/div[3]/a[1]/img').click() # 확인버튼

# main검색 버튼
driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/p[4]/input').click()


# 보고서들 제목, link
pageString = driver.page_source

reportLinkList = dartReportListParse(pageString)
reportLink = reportLinkList[0]['href']

driver.get(reportLink)
time.sleep(2)

bsobj = BeautifulSoup(driver.page_source, "html.parser")
downLinkBefore = bsobj.find("div", {"class":"view_search"}).find("a")['onclick']
downLoadLink = downloadLinkParse(downLinkBefore)
driver.get(downLoadLink)







