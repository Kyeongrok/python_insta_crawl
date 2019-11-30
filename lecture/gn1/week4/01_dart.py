from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path="../chrome/chromedriver74"
)

url = "http://dart.fss.or.kr/"

driver.get(url)

textCrpNm = driver.find_element_by_id("textCrpNm")
textCrpNm.send_keys("현대")

searchButton = driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/p[4]/input')
searchButton.click()

time.sleep(3)

# how to count trs

trs = driver.find_element_by_xpath('//*[@id="corpListContents"]/div/fieldset/div[1]/table/tbody').find_elements_by_tag_name('tr')


# for rowNum in range(1, len(trs) + 1):
#     driver.find_element_by_xpath('//*[@id="corpListContents"]/div/fieldset/div[1]/table/tbody/tr[{}]/td[1]'.format(rowNum))\
#         .find_element_by_css_selector('#checkCorpSelect').click()


