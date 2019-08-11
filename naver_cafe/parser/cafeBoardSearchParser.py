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
    if("없습니다." in trs[0].text):
        return 0
    return len(trs)

def parse2(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    boardBox = bsObj.find("table", {"class":"board-box"})
    trs = boardBox.find("tbody").findAll("tr")
    return len(trs)


