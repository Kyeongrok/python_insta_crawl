from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../chrome/chromedriver74")

url = "https://dart.fss.or.kr"

driver.get(url)

driver.find_element_by_xpath('//*[@id="textCrpNm"]').send_keys("현대")
driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/p[4]/input').click()

time.sleep(5)

pageString = driver.page_source
print(pageString)

driver.close()

file = open("companyinfo.html", "w", encoding="utf-8")
file.write(pageString)
