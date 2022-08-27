import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('admin123')
driver.find_element(By.XPATH,'//button[text()=" Login "]').click()

driver.find_element(By.XPATH,"//span[text()='Admin']").click()

ele=driver.find_element(By.XPATH,"//span[text()='User Management '] ")
users=driver.find_element(By.XPATH,"//a[text()='Users']")

actions=ActionChains(driver)

#MouseHover
actions.move_to_element(ele).move_to_element(users).click().perform()