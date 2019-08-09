from bs4 import BeautifulSoup

def getRow(tr):
    tds = tr.findAll("td")
    for td in tds:
        print(td)
    print(len(tds))

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    articleBoards = bsObj.findAll("div", {"class":"article-board m-tcol-c"})
    table = articleBoards[1].find("table")
    trs = table.find("tbody").findAll("tr")
    return len(trs)
