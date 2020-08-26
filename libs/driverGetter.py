import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# rootPath = os.path.split(os.environ['VIRTUAL_ENV'])[0]
def getDriver():
    rootPath = ".."
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path="{}/chrome/chromedriver75".format(rootPath),
        options=chrome_options
    )
    return driver

def getDriverWithPath(path):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path=path,
        options=chrome_options
    )
    return driver
