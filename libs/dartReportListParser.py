from bs4 import BeautifulSoup

def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    table = bsobj.find("div", {"class":"table_list"}).find("table")
    tbody = table.find("tbody")
    trs = tbody.findAll("tr")

    rows = []
    for tr in trs:
        tds = tr.findAll("td")
        title = tds[2].find("a")['title']
        href = tds[2].find("a")['href']
        row = {"title":title, "href":"http://dart.fss.or.kr"+href}
        rows.append(row)
    return rows

def downloadLinkParse(text):
    splitted1 = text.split(",")
    splitted2 = splitted1[0].split("(")[1]
    first = splitted2.replace("'","")
    second = splitted1[1].replace("'","").replace(")","").replace(" ","")
    link = "http://dart.fss.or.kr/pdf/download/main.do?rcp_no={}&dcm_no={}".format(first, second)
    return link

