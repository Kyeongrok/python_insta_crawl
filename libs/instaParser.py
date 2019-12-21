from bs4 import BeautifulSoup

def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    ezdmt = bsobj.find("div", {"class":"EZdmt"})
    v1Nh3List = ezdmt.findAll("div", {"class":"v1Nh3"})

    links = []
    for v1Nh3 in v1Nh3List:
        instaLink = "https://www.instagram.com"
        # <a href="123" alt="456">hi my name is ~~</a>
        linkAddr = v1Nh3.find("a")['href']
        links.append(instaLink + linkAddr)

    return links
