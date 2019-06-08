# urls.json을 불러옵니다.
# 불러온 url을 crawl해서 pages/n.html로 저장합니다.
import json
from libs.crawler import crawl
from threading import Thread
import time
import chardet

file = open("./urls.json")
urls = json.loads(file.read())
print(len(urls))

def crawlAndSave(url, index):
    print(index, url)
    pageString = crawl(url)

    # the_encoding = chardet.detect(pageString)['encoding']
    # print(the_encoding)

    file = open("./pages/{}.html".format(index), "w+")
    file.write(pageString.decode("utf-8"))
    file.close()

for fileNo in range(0, len(urls))[:1]:
    time.sleep(0.1)
    url = urls[fileNo]
    th = Thread(target=crawlAndSave, args=(url, fileNo))
    th.start()
