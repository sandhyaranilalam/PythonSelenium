import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
time.sleep(10)
driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
driver.close()       #-closes the current window which in focus
driver.quit()        #-kills all the window sessions,closes all the windows