import requests

def crawl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) 26.109 Safari/537.36"
    }
    data = requests.get(url, headers=headers)
    print(data, url)
    return data.content

