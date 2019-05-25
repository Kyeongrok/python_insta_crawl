from selenium import webdriver

rootPath = ".."
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver74".format(rootPath)
)

url = "https://www.facebook.com/"
driver.get(url)

driver.find_element_by_id("email").send_keys("oceanfog1@gmail.com")
# driver.find_element_by_id("pass").send_keys("123456")
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("1234556666")
driver.find_element_by_id("u_0_b").click()






