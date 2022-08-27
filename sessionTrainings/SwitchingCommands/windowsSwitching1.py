import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-input']").send_keys('selenium')
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
time.sleep(5)
links=driver.find_elements(By.PARTIAL_LINK_TEXT,'Selenium')
print(len(links))
for link in links:
    link.click()
windowIDS=driver.window_handles
for windid in windowIDS:
    driver.switch_to.window(windid)
    print(driver.title)
driver.quit()
