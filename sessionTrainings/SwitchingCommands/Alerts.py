import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
print(alert.text)
alert.dismiss()
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
print(alert.text)
alert.send_keys("welcome")
alert.accept()

driver.close()