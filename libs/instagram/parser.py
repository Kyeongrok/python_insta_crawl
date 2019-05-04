from bs4 import BeautifulSoup

def getPostInfo(post):
    aTag = post.find("a")
    link = "https://www.instagram.com{}".format(aTag["href"])
    return {"link":link}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    posts = bsObj.findAll("div", {"class":"v1Nh3"})
    postInfos = []
    for post in posts:
        postInfo = getPostInfo(post)
        postInfos.append(postInfo)
    return postInfos
