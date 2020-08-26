from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 사용 방법
# chrome하나를 debugger mode로 띄우고 로그인을 한 후 사용한다.

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome('../../chrome/chromedriver.exe', options=chrome_options)
def click_article_and_comment(notice, idx, comment, sleep_sec=2):
    driver.get(notice)
    time.sleep(sleep_sec)
    driver.switch_to.frame("cafe_main")

    print('{} clicked'.format(idx))
    # tr = driver.find_element_by_xpath('//*[@id="upperArticleList"]/table/tbody/tr[{}]'.format(idx)).find_element_by_tag_name('a')
    tr = driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[{}]'.format(idx)).find_element_by_tag_name('a')
    tr.click()
    time.sleep(sleep_sec)
    try:
        txtbox = driver.find_element_by_class_name('comment_inbox_text')
        txtbox.send_keys(comment)
        time.sleep(sleep_sec)
    except Exception as e:
        print('-----txt box 없음 -----')

    try:
        regist_button = driver.find_element_by_class_name('CommentWriter').find_element_by_class_name('btn_register')
        regist_button.click()
        time.sleep(sleep_sec)

    except Exception as e:
        print('----- button 없음-----')

comment = '확인했어요~^^'

# 페이지는 여기에서 바꿀 수 있음
page = '3'
# cafe의 댓글을 달고 싶은 게시판 주소를 notice에 넣는다.
# 뒷부분은 page={}로 할 것
notice = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=21031223&search.menuid=1&search.boardtype=L&search.totalCount=151&search.page={}'.format(page)
for no in range(1, 15):
    click_article_and_comment(notice, no, comment)

