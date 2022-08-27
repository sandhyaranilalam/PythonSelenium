import os

from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/login')
# driver.save_screenshot(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
driver.close()