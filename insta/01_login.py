from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver77".format(".."),
    options=chrome_options
)

url = "https://instagram.com/"
driver.get(url)
url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
driver.get(url)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')\
    .send_keys("oceanfog1@gmail.com")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').send_keys("1234@Aoeu")
# //*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button




