import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# declared at the begining and its applicable for all the elements in the script,default is 0 seconds
# it willnot wait entire timeperiod. if its availble within in the time it will jump to next statement. so no performance issue
# Disadvantage-if the element is not availble with in the time period then still there will be an exception
driver.implicitly_wait(10)

driver.get('https://www.google.co.in/')
driver.maximize_window()
searchBox = driver.find_element(By.XPATH,"//input[@title='Search']")
searchBox.send_keys("selenium")
searchBox.submit()#submit means pressing enter key

#time.sleep()--It waits till the time is completed so performnce of the script is poor and
# it will throw error if unable to find element within timeperiod

link = driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.quit()