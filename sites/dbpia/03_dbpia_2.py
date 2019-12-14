from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import urllib.request
import time

driver = webdriver.Chrome()
url = "http://www.dbpia.co.kr/"
driver.get(url)
time.sleep(3)

#close pop up window
driver.find_element_by_xpath("//*[@id='#pub_noticeLayerPopup13']").send_keys(Keys.ENTER)

key_word = '기술경영'
driver.find_element_by_css_selector('#keyword').send_keys(key_word) # .은 class, # 은 id
driver.find_element_by_css_selector('#keyword').send_keys(Keys.ENTER)

html = driver.page_source #currentpage 로 하지 말고 page_source 로 하자.
bs_obj = bs4.BeautifulSoup(html, 'html.parser')
'''
#####html 구조 ######
<ul class="list" id="dev_search_list">
    <li class="item">
        <div class="listBox">
            <span class="fCheck">
                <a href="#none" class="disabled btnCheckboxTooltip">
                    <span class="checkboxTooltip">이용권한이 없거나, 링크만 제공되는 자료입니다.
                    </span>
                </a>
            <input type="checkbox" id="pub_check_0" class="checkButtonActive disabled" value="NODE09216239">
            <label for="pub_check_0">
                <span class="blind">체크박스
                </span>
            </label>
            </span>
        <div class="typeWrap">
            <ul class="type">
                <li class="data">학술저널
                </li>
                <li class="use">구매가능
                </li>
            </ul>
        </div>
        <div class="titWrap">
            <h5>
                <a href="/journal/articleDetail?nodeId=NODE09216239" target="_blank">혁신 및 
                    <font color="red">기술경영
                    </font> 
                    역량에 따른 중소기업의 고용효과 비교분석 - 
                    <font color="red">기술
                    </font>
                    금융 
                    <font color="red">기술
                    </font>
                    력 평가 대상 중소기업을 중심으로 -
                </a>
            </h5>
            <span class="stats">이용수
                <small>24
                </small>
            </span>
        </div>
        <ul class="info"> .... </ul>
        <div class="btnWrap">...</div>
        <input id="doi_code" type="hidden" value="10.34122/jip.2019.09.14.3.233">
        </div>
    </li>
    <li class="item">...</li>
    <li class="item">...</li>
    <li class="item">...</li>
    <li class="item">...</li>
    <li class="item">...</li>

'''

# HTML 에서 논문제목과 저자만 텍스트로 뽑아보자.
# 궁금한점: 여러단에 걸처 하위에 있는 클래스는 바로 앞단까지 하나씩 찾아내려가야하는가
# 아니면 상위클래스를 불러오면 여러단 아래의 정보까지 다 찾을 수 있는가.... --> 아직 모르겠음.

r = bs_obj.find_all('ul',{'class':'list'}) #<ul class="list" id="dev_search_list">
print(r)
lists = r.findAll('li') # li class="item" --> 게시물 하나씩을 포함하는 클래스
list_box = lists.findAll('div',{"class": "listBox"}) # 게시물의 원하는 정보가 다 listbox 클래스 하위에 있다.
titWrap = list_box.findAll('div',{'class':'titWrap'}) # 여기서는 제목을 갖고 오자
info = list_box.findAll('ul',{'class':'info'}) # 여기서는 지은이를 갖고오자.

for title in titWrap:
    h5_tag = title.find('h5') # 논문 제목이 h5 태그 하위에 a href= 에 들어있음.
    print(h5_tag.a.attrs['href'])

for who in info:
    name = who.find('author')
    print(name.a.attrs['href'])