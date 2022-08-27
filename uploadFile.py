from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.monsterindia.com/')
driver.find_element(By.XPATH,"//span[text()='Upload Resume']").click()
driver.find_element(By.XPATH,'//input[@id="file-upload"]').send_keys("C:\Users\DELL\Downloads\file-example_PDF_1MB.pdf")
