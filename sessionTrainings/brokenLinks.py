from selenium import webdriver
import requests as requests
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://www.deadlinkcity.com/')
links=driver.find_elements(By.TAG_NAME,'a')
c=0
for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print('brokenlink:',url)
        c += 1
    else:
        print('valid link:',url)
print('countofbrokenLinks:',c)
driver.close()