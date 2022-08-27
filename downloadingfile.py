from selenium import webdriver
import os, time

from selenium.webdriver.common.by import By

location = os.getcwd()
print(location)
# prefrences = {"download.default_directory": location}
opt = webdriver.ChromeOptions()
# opt.add_experimental_option('prefs', prefrences)
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
try:
    driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
    elem = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div/div[2]/div/div/table/tbody/tr[1]/td[5]/a')
    print(elem.text)
    elem.click()

    time.sleep(5)
except:
    pass
finally:
    driver.close()
