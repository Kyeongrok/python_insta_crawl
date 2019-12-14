# selenium으로 instagram열기

from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    executable_path="../../chrome/chromedriver77"
)

url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
driver.get(url)

time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("oceanfog1@gmail.com")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("1234@Asdf")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

time.sleep(3)
# popup
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

# search
time.sleep(2)
url = "https://www.instagram.com/explore/tags/축구/"
driver.get(url)

time.sleep(2)

def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    ezdmt = bsobj.find("div", {"class":"EZdmt"})
    v1Nh3List = ezdmt.findAll("div", {"class":"v1Nh3"})

    for v1Nh3 in v1Nh3List:
        instaLink = "https://www.instagram.com"
        # <a href="123" alt="456">hi my name is ~~</a>
        linkAddr = v1Nh3.find("a")['href']
        print(instaLink + linkAddr)

pageString = driver.page_source
links = parse(pageString)
print(links)

# link뽑기
