import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://admin::admin@the-internet.herokuapp.com/basic_auth')
time.sleep(5)
driver.close()