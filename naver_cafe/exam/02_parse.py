from bs4 import BeautifulSoup

file = open("./searchResult.html")
pageString = file.read()


bsObj = BeautifulSoup(pageString, "html.parser")
articleBoards = bsObj.findAll("div", {"class":"article-board m-tcol-c"})
print(articleBoards[1])
print(len(articleBoards))
