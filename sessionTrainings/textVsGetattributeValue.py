from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/login')
username=driver.find_element(By.ID,'Email')

print('text:',username.text)        #----- text always returns inner text of the element if its avaialble else it will not return anything
print('getattributeValue:',username.get_attribute('name'))   #--- get_attribute always returns the value ofthe attribute we passed
