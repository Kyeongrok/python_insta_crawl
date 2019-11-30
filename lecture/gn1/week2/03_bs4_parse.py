from selenium import webdriver
from time import sleep
from libs.instagram.parser import parse

def getInstaPageSource():
    rootPath = ".."
    driver = webdriver.Chrome(
        executable_path="{}/chrome/chromedriver77".format(rootPath)
    )
    url = "https://www.instagram.com/explore/tags/운동스타그램/"
    driver.get(url)
    sleep(5) # 5초 기다렸다가 스크롤
    driver.execute_script(
        'window.scrollTo(0, document.body.scrollHeight)')
    sleep(2)
    driver.execute_script(
        'window.scrollTo(0, document.body.scrollHeight)')
    sleep(2)
    pageString = driver.page_source
    driver.close()
    return pageString

pageString = getInstaPageSource()
posts = parse(pageString)
print(posts)

# file = open("./insta운동스타그램.html", "w+", encoding="utf-8")
# file.write(pageString)

# posts = parse(pageString)
# print(pageString)


