# 04/29/2020
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/robertjohnson/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
print(driver.title)

search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()