from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')

ele=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
act=ActionChains(driver)
act.context_click(ele).perform()
driver.close()