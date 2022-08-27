import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys('Admin')
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('admin123')
driver.find_element(By.XPATH,'//button[text()=" Login "]').click()

driver.find_element(By.XPATH,"//span[text()='Admin']").click()
driver.find_element(By.XPATH,"//span[text()='User Management '] ").click()
driver.find_element(By.XPATH,"//a[text()='Users']").click()
time.sleep(10)
elements=driver.find_elements(By.XPATH,"//div[@class='orangehrm-container']/div/div/div")
noOfDivs=len(elements)
print((noOfDivs))
time.sleep(5)
enabledCount,disablecount=0,0
print(driver.find_element(By.XPATH,"//div[@class='orangehrm-container']/div/div/div[1]/div/div/div[2]/div[3]/div/div[2]").text)
# for i in range(1,noOfDivs):
#     status=driver.find_element(By.XPATH,"//div[@class='orangehrm-container']/div/div/div[" + str(i) + "]/div/div/div[2]/div[3]/div/div[2]").text
#     if status=='Enabled':
#         empname=driver.find_element(By.XPATH,"//div[@class='orangehrm-container']/div/div/div[" + str(i) + "]/div/div/div/div/div/div/div[2]")
#         print("employee Name:",empname.text)
#         enabledCount+=1
#     else:
#         disablecount+=1
# print(enabledCount,disablecount)
driver.close()
