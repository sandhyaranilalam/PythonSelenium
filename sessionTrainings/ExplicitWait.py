from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
'''Explicit wait waits for the condition to be satisfied'''
mywait = WebDriverWait(driver,10,ignored_exceptions=[Exception])   #Syntax
'''#if there is an exception then it will be ignored with explicit'''
driver.get('https://www.google.co.in/')
driver.maximize_window()
searchBox = driver.find_element(By.XPATH,"//input[@title='Search']")
searchBox.send_keys("selenium")
searchBox.submit()#submit means pressing enter key


ele=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
ele.click()

driver.quit()

'''Advantage
more effective,

dis:
need to insert at multiple places'''


