# thread -> 일 하는 사람
# 기본값은 일 하는 사람 = 1명
# 스레드가 실행 하는 것 = function(함수)
from threading import Thread
from time import sleep
import json
from libs.crawler import crawl
import time

file = open("urls.json")
urlsString = file.read()
urls = json.loads(urlsString)

def printHello(url, num):
    pageString = crawl(url)
    file = open("./pages2/{}.html".format(num), "w+", encoding="euc-kr")
    file.write(str(pageString))
    file.close()

for i in range(0, 1000):
    url = urls[i]
    th = Thread(target=printHello, args=(url, i))
    th.start()
    sleep(0.01)
