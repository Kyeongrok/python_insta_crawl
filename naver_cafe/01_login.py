from libs.driverGetter import getDriver
import time

driver = getDriver()

url = "https://www.naver.com/"

driver.get(url)

driver.find_element_by_xpath('//*[@id="account"]/div/a').click()

#id
driver.find_element_by_xpath('//*[@id="id"]').send_keys("oceanfog")

driver.find_element_by_xpath('//*[@id="pw"]').send_keys("1234@Aoeu")
# login button
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(25)


url = "https://cafe.naver.com/joonggonara"
driver.get(url)

keyword = "감기"
driver.find_element_by_xpath('//*[@id="topLayerQueryInput"]').send_keys(keyword)
driver.find_element_by_xpath('//*[@id="cafe-search"]/form/button').click()

driver.switch_to_frame("cafe_main")
time.sleep(3)

pageString = driver.page_source

file = open("./joonggonara_gamgi.html", "w+")
file.write(pageString)


time.sleep(30)
driver.close()
