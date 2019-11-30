from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="../chrome/chromedriver77" # .exe
)

url = "https://krksap.tistory.com/manage"
driver.get(url)

xpath = '//*[@id="loginId"]'
driver.find_element_by_xpath(xpath).send_keys("abc_hello@gmail.com")
driver.find_element_by_xpath('//*[@id="loginPw"]').send_keys("abcd_1234")

# login button click
driver.find_element_by_xpath('//*[@id="authForm"]/fieldset/button').click()

print(driver.page_source)

