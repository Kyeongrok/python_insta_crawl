import requests
from fake_useragent import UserAgent

def crawl(url):
    ua = UserAgent()
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 26.109 Safari/537.36"
    userAgent = ua.random
    headers = {
        "User-Agent": agent
    }
    data = requests.get(url, headers=headers)
    print(data, url)
    return data.content

