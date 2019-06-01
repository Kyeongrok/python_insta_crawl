from bs4 import BeautifulSoup

def parse(pagestring):
    bsobj = BeautifulSoup(pagestring, "html.parser")
    title = bsobj.find("h2", {"class":"prod-buy-header__title"})
    reviewers = bsobj.find("span",{"class":"prod-buy-header__productreview"})
    count = reviewers.find("span", {"class":"count"})
    return {"title":title.text, "count":count.text}
