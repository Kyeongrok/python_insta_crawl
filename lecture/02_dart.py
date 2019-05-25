import time

from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="../chrome/chromedriver74"
)

url = "http://dart.fss.or.kr/"

driver.get(url)

driver.find_element_by_id("textCrpNm").send_keys("셀트리온")
driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/p[4]/input').click()

time.sleep(5)
print("----5sec end----")
driver.find_element_by_xpath('//*[@id="checkCorpSelect"]').click()
driver.find_element_by_xpath('//*[@id="corpListContents"]/div/fieldset/div[3]/a[1]/img').click()

#두번째 검색버튼
driver.find_element_by_xpath('//*[@id="searchpng"]').click()

pageString = driver.page_source
print(pageString)

time.sleep(10)
print("----10sec end----")
driver.close()