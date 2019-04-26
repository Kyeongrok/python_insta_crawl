import os
from selenium import webdriver

rootPath = os.path.split(os.environ['VIRTUAL_ENV'])[0]
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver".format(rootPath),
)

url = "https://instagram.com/"
driver.get(url)
driver.close()
