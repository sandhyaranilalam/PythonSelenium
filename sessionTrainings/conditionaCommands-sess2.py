import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()
element=driver.find_element(By.ID,'small-searchterms')

print('isdisplayed:',element.is_displayed())  # isDisplayed
print('isenabled:',element.is_enabled())      #isEnabled

rd_male=driver.find_element(By.XPATH,"//label[@for='gender-male']")
rd_female=driver.find_element(By.XPATH,"//label[@for='gender-female']")
print("rd_male:",rd_male.is_selected())
print("rd_female:",rd_female.is_selected())
rd_female.click()
time.sleep(10)
#After selecting radio button
print("rd_male:",rd_male.is_selected())
print("rd_female:",rd_female.is_selected())

driver.close()
