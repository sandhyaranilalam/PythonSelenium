from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as keys

driver=webdriver.Chrome()
driver.get('https://text-compare.com/')
txtbox1=driver.find_element(By.ID,'inputText1')
txtbox2=driver.find_element(By.ID,'inputText2')

txtbox1.send_keys("sandhya is good girl")

act=ActionChains(driver)
act.key_down(keys.CONTROL).send_keys('a').key_up(keys.CONTROL).perform()
act.key_down(keys.CONTROL).send_keys('c').key_up(keys.CONTROL).perform()
act.send_keys(keys.TAB).perform()
act.key_down(keys.CONTROL).send_keys('v').key_up(keys.CONTROL).perform()
driver.close()







