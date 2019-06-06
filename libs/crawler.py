import requests

def crawl(url):
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 26.109 Safari/537.36"
    headers = {
        "User-Agent": agent
    }
    data = requests.get(url, headers=headers)
    # data = requests.get(url)
    print(data, url)
    return data.content

