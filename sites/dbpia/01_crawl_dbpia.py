import requests
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import urllib.request
import time

path = os.getcwd()+"/../../chrome/chromedriver77"

driver = webdriver.Chrome(
    executable_path=path
)

url = "http://www.dbpia.co.kr/"
driver.get(url)
time.sleep(5)

#close pop up window
driver.find_element_by_xpath("//*[@id='#pub_noticeLayerPopup13']").send_keys(Keys.ENTER)



key_word = '기술경영'
driver.find_element_by_css_selector('#keyword').send_keys(key_word) # .은 class, # 은 id
driver.find_element_by_css_selector('#keyword').send_keys(Keys.ENTER)

time.sleep(2)
html = driver.page_source
print('html:', html)

bs_obj = bs4.BeautifulSoup(html, 'html.parser')
# print('bs_obj:', bs_obj)

uls = bs_obj.find_all("ul", {"class":"list"})
# uls = bs_obj.find("ul", {"class":"list"})
print('ul:', uls)