import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# rootPath = os.path.split(os.environ['VIRTUAL_ENV'])[0]
rootPath = ".."
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver".format(rootPath),
    options=chrome_options
)
driver.implicitly_wait(5)

def parse(pageString):

    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("div", {"class":"Nnq7C weEfm"})
    print(ul)

url = "https://instagram.com/explore/tags/발레"
print(url)
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".Nnq7C"))
)
pageString = driver.page_source
parse(pageString)
driver.close()

