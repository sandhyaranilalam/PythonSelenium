import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('admin123')
driver.find_element(By.XPATH,'//button[text()=" Login "]').click()
act_title=driver.title
exp_title='OrangeHRM'
if act_title==exp_title:
    print('logged in successfull')
else:
    print('login failed')
# driver.close()