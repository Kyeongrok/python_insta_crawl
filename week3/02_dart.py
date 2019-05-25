from selenium import webdriver

rootPath = ".."
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver74".format(rootPath),
)
 
url = "http://dart.fss.or.kr/"
driver.get(url)

driver.find_element_by_id("textCrpNm")\
    .send_keys("셀트리온")

driver.find_element_by_xpath("//*[@id='searchForm']/fieldset/p[4]/input")\
    .click()
pageString = driver.page_source
print(pageString)


