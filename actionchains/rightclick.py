import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

ele=driver.find_element(By.XPATH,"//span[text()='right click me']")

act=ActionChains(driver)
act.context_click(ele).perform()

time.sleep(10)
driver.find_element(By.XPATH,"//span[text()='Copy']").click()

driver.switch_to.alert.accept()
driver.close()