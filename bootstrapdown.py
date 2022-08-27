import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
time.sleep(10)
driver.find_element(By.XPATH,'//span[@id="select2-billing_country-container"]').click()
countrylist=driver.find_elements(By.XPATH,'//span[@class="select2-results"]/ul/li')
countries=len(countrylist)

for country in countrylist :
    if country.text=='Indonesia':
        country.click()
        break
driver.close()