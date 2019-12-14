
text = "openPdfDownload('20191213000488', '6996117')"

def downloadLinkParse(text):
    splitted1 = text.split(",")
    splitted2 = splitted1[0].split("(")[1]
    first = splitted2.replace("'","")
    second = splitted1[1].replace("'","").replace(")","").replace(" ","")
    link = "http://dart.fss.or.kr/pdf/download/main.do?rcp_no={}&dcm_no={}".format(first, second)
    return link

print(downloadLinkParse(text))