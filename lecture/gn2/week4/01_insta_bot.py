from selenium import webdriver
from libs.instaParser import parse
import time

# 1.instagram 로그인 페이지로 접속
# 2.id, pw입력
# 3.특정 hash tag로 검색한 페이지로 이동하기
# 4.해당 페이지에서 각 포스트의 링크 뽑기
driver = webdriver.Chrome(
    executable_path="../../../chrome/chromedriver78"
)
url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
driver.get(url)

time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("oceanfog1@gmail.com")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("asdf@1234")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

time.sleep(2)
url = "https://www.instagram.com/explore/tags/발레/"
driver.get(url)

# 스크롤 하기
for scrollN in range(2):
    driver.execute_script(
        'window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)

time.sleep(5)

pageString = driver.page_source

file = open("insta.html", "w+", encoding="utf-8")
file.write(pageString)

for link in parse(pageString):
    time.sleep(1)
    driver.get(link)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span').click()


