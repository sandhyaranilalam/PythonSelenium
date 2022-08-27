from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.find_element(By.XPATH,'//input[@name="dob"]').click()

month=Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]'))
month.select_by_visible_text('Apr')

year=Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-year"]'))
year.select_by_visible_text('1994')

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text =='20':
        date.click()
        break
driver.close()