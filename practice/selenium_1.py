# 04/29/2020
from selenium import webdriver

PATH = "/Users/robertjohnson/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
