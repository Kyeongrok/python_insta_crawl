from selenium import webdriver
import time
driver = webdriver.Chrome(
    executable_path="../chrome/chromedriver77"
)

url = "https://www.instagram.com/explore/tags/맛집/"
driver.get(url)
time.sleep(2)
pageString = driver.page_source

open("ballet.html", "w+", encoding="utf-8").write(pageString)

