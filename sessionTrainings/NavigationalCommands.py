from selenium import webdriver

driver=webdriver.Chrome()

driver.get('https://www.amazon.in/your-account')
driver.get('https://www.snapdeal.com/login')

#Navigational commands
driver.back()
driver.forward()
driver.refresh()

driver.quit()