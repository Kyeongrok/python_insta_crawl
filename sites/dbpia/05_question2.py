import urllib.request
from bs4 import BeautifulSoup

url='https://finance.naver.com/item/board.nhn?code=000660'
html=urllib.request.urlopen(url)

bsobj=BeautifulSoup(html,'html.parser')

divs=bsobj.find_all ('td',{'class':'title'})

for div in divs:
    print(div.text)

savename="tete.csv"
with open(savename, 'a') as f:
    for i in range(1,100):
        f.write(div[i].text)
        print("complete")