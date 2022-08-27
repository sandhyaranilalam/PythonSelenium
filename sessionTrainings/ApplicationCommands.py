from selenium import webdriver

driver=webdriver.Chrome()

#application commands--   title, current_url,page_source

driver.get('https://opensource-demo.orangehrmlive.com/')

title=driver.title
currentUrl=driver.current_url
pageSource=driver.page_source

print(title,currentUrl,pageSource)

driver.close()


