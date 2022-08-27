from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()
#Using select class
dropdowns=Select(driver.find_element(By.ID,'input-country'))
#dropdowns.select_by_index(2)
#dropdowns.select_by_value('8')
#dropdowns.select_by_visible_text('Austria')

#without selectclassmethods
Alloptions=dropdowns.options
for option in Alloptions:
    option.text=='India';
    option.click()
    break

driver.close()

