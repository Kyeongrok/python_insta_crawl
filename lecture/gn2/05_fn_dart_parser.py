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