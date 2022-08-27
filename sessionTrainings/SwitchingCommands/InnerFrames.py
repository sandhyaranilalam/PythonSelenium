import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
button=driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe")
button.click()
outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
innerframe=driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(innerframe)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")
driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.close()

