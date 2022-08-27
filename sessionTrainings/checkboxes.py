from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://itera-qa.azurewebsites.net/home/automation')
checkobxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
#print(len(checkobxes))

# #1) select all the checkboxes
for i in checkobxes:
    i.click()

# #2) select check boxes by choice

for i in checkobxes:
    if i.get_attribute('id')=='monday' or i.get_attribute('id')=='friday':
        i.click()

#3) select last two checkboxes:
for i in range(len(checkobxes)-2,len(checkobxes)):
    checkobxes[i].click()

#4) ) select last two checkboxes:
for i in range(len(checkobxes)):
    if i <2:
        checkobxes[i].click()

#5) Unselect all the checkboxes
for i in checkobxes:
    if i.is_selected():
        i.click()

driver.close()