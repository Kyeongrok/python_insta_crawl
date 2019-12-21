# selenium으로 instagram열기

from selenium import webdriver
import time, random
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    executable_path="../../chrome/chromedriver78"
)

url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
driver.get(url)

time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("oceanfog1@gmail.com")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("asdf@1234")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

# time.sleep(3)
# popup
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

# search
time.sleep(2)
url = "https://www.instagram.com/explore/tags/게임/"
driver.get(url)


def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    ezdmt = bsobj.find("div", {"class":"EZdmt"})
    v1Nh3List = ezdmt.findAll("div", {"class":"v1Nh3"})

    links = []
    for v1Nh3 in v1Nh3List:
        instaLink = "https://www.instagram.com"
        # <a href="123" alt="456">hi my name is ~~</a>
        linkAddr = v1Nh3.find("a")['href']
        links.append(instaLink + linkAddr)

    return links

time.sleep(3)
pageString = driver.page_source
links = parse(pageString)

# 좋아요 누르고 댓글 달기
for url in links:
    try:
        print(url)
        driver.get(url)

        rndSec = random.randint(5, 15)
        time.sleep(rndSec)
        message = "잘 보고 갑니다. 오늘 날씨가 너무 좋네요. 제 인스타도 놀러와주세요. 맞팔 신청합니다."
        #driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys(message)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/button').click()
    except Exception as e:
        pass


# driver.close()
# link뽑기
