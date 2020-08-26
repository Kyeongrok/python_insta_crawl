from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome('../../chrome/chromedriver.exe', options=chrome_options)
notice = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=21031223&search.menuid=1&search.boardtype=L&search.totalCount=151&search.page=1'

def click_article_and_comment(idx, comment, sleep_sec=2):
    driver.get(notice)
    time.sleep(sleep_sec)
    driver.switch_to.frame("cafe_main")

    print('{} clicked'.format(idx))
    tr = driver.find_element_by_xpath('//*[@id="upperArticleList"]/table/tbody/tr[{}]'.format(idx)).find_element_by_tag_name('a')
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

    except Exception as e:
        print('----- button 없음-----')

comment = '확인했어요~^^'

click_article_and_comment(13, comment)

