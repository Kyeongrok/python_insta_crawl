from libs.driverGetter import getDriver
import time

driver = getDriver()

url = "https://www.naver.com/"
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
driver.get(url)

driver.find_element_by_xpath('//*[@id="id"]').send_keys("oceanfog")
driver.find_element_by_xpath('//*[@id="pw"]').send_keys("1234@Aoeu")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

time.sleep(20)

url = "https://cafe.naver.com/joonggonara"
driver.get(url)

keyword = "감기"
driver.find_element_by_xpath('//*[@id="topLayerQueryInput"]').send_keys(keyword)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="cafe-search"]/form/button').click()


url = "https://cafe.naver.com/ArticleSearchList.nhn?search.clubid=10050146&search.searchBy=0&search.query=%B0%A8%B1%E2"
driver.get(url)
time.sleep(2)
driver.switch_to_frame("cafe_main")

pageString = driver.page_source
print(pageString)


