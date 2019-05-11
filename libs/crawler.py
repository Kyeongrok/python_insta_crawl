import requests

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

