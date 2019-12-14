from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path="../../chrome/chromedriver77"
)

url = "https://nid.naver.com/nidlogin.login"
driver.get(url)

driver.find_element_by_xpath('//*[@id="id"]').send_keys("oceanfog")
driver.find_element_by_xpath('//*[@id="pw"]').send_keys("1234asdf")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# 로그인은 수동
time.sleep(40)

url = "https://cafe.naver.com/singaporelove"
driver.get(url)
