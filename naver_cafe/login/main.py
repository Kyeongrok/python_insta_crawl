from libs.driverGetter import getDriverWithPath



driver = getDriverWithPath('../../chrome/chromedriver.exe')


login_url = 'https://nid.naver.com/nidlogin.login'
driver.get(login_url)
driver.find_element_by_xpath('//*[@id="id"]').send_keys('rs_hansung')
driver.find_element_by_xpath('//*[@id="pw"]').send_keys('')




cafe_url = 'https://cafe.naver.com/gimhaezumma?iframe_url_utf8=%2FArticleRead.nhn%253Farticleid%3D1706801%2526clubid%3D21031223'
driver.get(cafe_url)



