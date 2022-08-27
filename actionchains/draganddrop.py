from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
act=ActionChains(driver)
src1=driver.find_element(By.XPATH,'//div[@id="box6"]')
trgt1=driver.find_element(By.XPATH,'//div[text()="Italy"]')

act.drag_and_drop(src1,trgt1).perform()

src2=driver.find_element(By.XPATH,"//div[@id='box3']")
targt2=driver.find_element(By.XPATH,"//div[text()='United States']")

act.drag_and_drop(src2,targt2).perform()

driver.close()

