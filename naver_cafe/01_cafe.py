from libs.driverGetter import getDriver
import time

driver = getDriver()

url = "https://www.naver.com/"
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
driver.get(url)

driver.find_element_by_xpath('//*[@id="id"]').send_keys("oceanfog")
driver.find_element_by_xpath('//*[@id="pw"]').send_keys("ㅈ")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

time.sleep(12)

url = "https://cafe.naver.com/joonggonara"
driver.get(url)

keyword = "감기"
driver.find_element_by_xpath('//*[@id="topLayerQueryInput"]').send_keys(keyword)
driver.find_element_by_xpath('//*[@id="cafe-search"]/form/button').click()




