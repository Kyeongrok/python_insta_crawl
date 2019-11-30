from selenium import webdriver
from time import sleep

def getInstaPageSource():
    rootPath = ".."
    driver = webdriver.Chrome(
        executable_path="{}/chrome/chromedriver77".format(rootPath)
    )

    url = "https://www.instagram.com/explore/tags/운동스타그램/"
    url = "https://www.instagram.com/p/B3R_QUSgCnP/"
    driver.get(url)

    # 10초 후에 닫히게 해보세요. hint) time.sleep
    sleep(5)
    pageString = driver.page_source

    driver.close()
    return pageString

pageString = getInstaPageSource()
print(pageString)

