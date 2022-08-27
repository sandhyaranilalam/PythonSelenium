from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
windowID=driver.current_window_handle
print(windowID)
windowIDs=driver.window_handles
print(len(windowIDs))
# driver.switch_to.window(windowIDs[0])
# print(driver.title)
# driver.switch_to.window(windowIDs[1])
# print(driver.title)

'''switching between windows'''
# for windowId in windowIDs:
#     driver.switch_to.window(windowId)
#     print(driver.title)

'''to close a particular window'''
for windid in windowIDs:
    driver.switch_to.window(windid)
    if driver.title=='OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM':
        driver.close()
