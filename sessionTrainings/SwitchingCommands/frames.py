import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
time.sleep(5)
driver.switch_to.frame('packageListFrame')
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame('classFrame')
driver.find_element(By.XPATH,"//div[@class='fixedNav']/div[2]/ul[1]/li[1]/a").click()
driver.switch_to.default_content()

driver.close()