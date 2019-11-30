from bs4 import BeautifulSoup

file = open("ballet.html", encoding="utf-8")
pageString = file.read()
# 010 3588 6265
def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    ezdmt = bsobj.find("div", {"class":"EZdmt"})
    v1Nh3List = ezdmt.findAll("div", {"class":"v1Nh3"})

    for v1Nh3 in v1Nh3List:
        instaLink = "https://www.instagram.com"
        # <a href="123" alt="456">hi my name is ~~</a>
        linkAddr = v1Nh3.find("a")['href']
        print(instaLink + linkAddr)

parse(pageString)