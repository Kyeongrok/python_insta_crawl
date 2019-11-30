from selenium import webdriver

rootPath = ".."
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver77".format(rootPath),
)

url = "https://www.facebook.com/"
driver.get(url)

driver.find_element_by_class_name("inputtext")\
    .send_keys("oceanfog1@gmail.com")

driver.find_element_by_id("u_0_3").click()


