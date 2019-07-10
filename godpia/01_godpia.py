from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
# chrome_options.add_argument("--headless")

rootPath = ".."
driver = webdriver.Chrome(
    executable_path="{}/chrome/chromedriver74".format(rootPath),
    options=chrome_options
)

url = "http://bible.godpia.com/write/sub020301.asp?cb_idx=602"
driver.get(url)

driver.find_elements_by_class_name("h-btn01")[1]\
    .find_element_by_class_name("clickNavMenu").click()


driver.find_element_by_id("inputID")\
     .send_keys("oceanfog")
driver.find_element_by_id("inputPW") \
    .send_keys("")

driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/a/img").click()

mrkUrl = "http://bible.godpia.com/write/sub020302.asp?cb_idx=602&ver=gae&vol=mrk&chap=2&secindex=1"
driver.get(mrkUrl)

ul = driver.find_element_by_class_name("write").find_element_by_tag_name("ul")
lis = ul\
    .find_elements_by_tag_name("li")

print("lis:", len(lis))

for index in range(0, len(lis)):

    li = lis[index]
    ps = li.find_elements_by_tag_name("p")

    statement = ps[0].text
    print(statement)
    textarea = ps[1].find_element_by_tag_name("textarea")
    time.sleep(4)
    textarea.send_keys(statement)
    time.sleep(4)
    textarea.send_keys(Keys.RETURN)
    time.sleep(3)


# driver.close()




