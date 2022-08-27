from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_argument('--disable--notifications')
driver=webdriver.Chrome(options=options)
driver.get('https://whatmylocation.com/')
driver.close()