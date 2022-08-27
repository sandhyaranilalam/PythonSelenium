import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()

# scroll down by pixel
#
# driver.execute_script("window.scrollBy(0,3000)","")
# pixelvalue=driver.execute_script("return window.pageYOffset;")
# print(pixelvalue)

#  scroll till he element is visisble
# ele=driver.find_element(By.XPATH,'//img[@alt="Flag of India"]')
# driver.execute_script("arguments[0].scrollIntoView();",ele)

# #scroll bottom of the page
#
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(10)
#Scroll to Top
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

#driver.close()