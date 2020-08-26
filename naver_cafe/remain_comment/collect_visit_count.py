from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# 30분마다 카페 방문하기
# 사용 방법
# chrome하나를 debugger mode로 띄우고 로그인을 한 후 사용한다.
# 아래 urls에 방문할 cafe주소를 넣는다.

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('../../chrome/chromedriver.exe', options=chrome_options)

# cafe방문
# '나의 활동' 클릭
# 방문 횟수 구하기
def print_visit_cnt(url):
    driver.get(url)
    time.sleep(2)
    xpath_my_activity = '//*[@id="cafe-info-data"]/ul/li[3]/p/a'
    driver.find_element_by_xpath(xpath_my_activity).click()
    time.sleep(1)
    xpath_visit_cnt = '//*[@id="ia-action-data"]/div[2]/ul/li[1]/em'
    visit_cnt = driver.find_element_by_xpath(xpath_visit_cnt).text
    print(url, visit_cnt, datetime.now())
    time.sleep(2)

urls = [
    'http://cafe.naver.com/mp3musicdownloadcafe',
    'https://cafe.naver.com/shopjirmsin'
]
for _ in range(5):
    for url in urls:
        print_visit_cnt(url)
    time.sleep(60 * 31) # 60초 * 30