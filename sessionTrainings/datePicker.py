from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://jqueryui.com/datepicker/')

driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
month = "October"
year = "2022"
day="29"
while True:
    mon = driver.find_element(By.XPATH,'//span[@class="ui-datepicker-month"]').text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH,"//span[text()='Next']").click()

#day:
dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text == day:
        date.click()
        break
