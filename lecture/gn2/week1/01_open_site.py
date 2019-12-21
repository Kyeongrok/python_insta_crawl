from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="../../chrome/chromedriver77"
)

# open site
url = "https://www.dbpia.co.kr/"
driver.get(url)

driver.find_element_by_xpath('//*[@id="#pub_noticeLayerPopup13"]').click()
driver.find_element_by_xpath('//*[@id="#pub_modalOrganPop"]').click()
driver.find_element_by_xpath('//*[@id="#pub_modalLoginPop"]').click()

driver.find_element_by_xpath('//*[@id="keyword"]').send_keys("의료")
driver.find_element_by_xpath('//*[@id="header"]/div[4]/div[2]/div[1]/div[1]/a').click()

import time
time.sleep(2)
pageString = driver.page_source
print(pageString)