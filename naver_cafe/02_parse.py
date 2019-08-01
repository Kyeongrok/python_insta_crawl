from bs4 import BeautifulSoup

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    articleBoards = bsObj.findAll("div", {"class":"article-board result-board m-tcol-c"})
    print(articleBoards)
    print(len(articleBoards))



    return []

file = open("joonggonara_gamgi.html")
pageString = file.read()
list = parse(pageString)