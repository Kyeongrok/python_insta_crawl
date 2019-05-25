import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

def getPost(div):
    aTag = div.find("a")
    link = "https://www.instagram.com{}".format(aTag['href'])
    print(link)

    return {}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("div", {"class":"EZdmt"})
    lis = ul.findAll("div", {"class":"v1Nh3"})
    li = lis[0]
    print(getPost(li))


def crawl():
    # rootPath = os.path.split(os.environ['VIRTUAL_ENV'])[0]
    rootPath = ".."
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path="{}/chrome/chromedriver73".format(rootPath),
        options=chrome_options
    )

    url = "https://instagram.com/explore/tags/발레"
    print(url)
    driver.get(url)

    # wait = WebDriverWait(driver, 2)
    # wait.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, ".EZdmt"))
    # )
    sleep(5)
    pageString = driver.page_source
    driver.close()
    return pageString

pageString = crawl()
parse(pageString)

