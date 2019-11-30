from selenium import webdriver

rootPath = ".."
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver74".format(rootPath),
)

url = "https://www.facebook.com/"
driver.get(url)

driver.find_element_by_class_name("inputtext")\
    .send_keys("oceanfog1@gmail.com")

password = driver.find_element_by_id("pass")
password.send_keys("123456")

loginButton = driver.find_element_by_id("u_0_b")
loginButton.click()

pageString = driver.page_source
print(pageString)


