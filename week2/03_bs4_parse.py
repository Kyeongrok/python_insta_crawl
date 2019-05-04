from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

def getInstaPageSource():
    rootPath = ".."
    driver = webdriver.Chrome(
        executable_path="{}/chrome/chromedriver74".format(rootPath)
    )

    url = "https://www.instagram.com/explore/tags/운동스타그램/"
    driver.get(url)

    # 10초 후에 닫히게 해보세요. hint) time.sleep
    sleep(5)
    pageString = driver.page_source

    driver.close()
    return pageString



pageString = getInstaPageSource()

file = open("./insta운동스타그램.html", "w+", encoding="utf-8")
file.write(pageString)

# posts = parse(pageString)
# print(pageString)


