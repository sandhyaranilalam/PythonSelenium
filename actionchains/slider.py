from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
act=ActionChains(driver)
minSlider=driver.find_element(By.XPATH,'//div[@class="price-range-block"]/div[2]/span[1]')
maxSlider=driver.find_element(By.XPATH,'//div[@class="price-range-block"]/div[2]/span[2]')

print("locations before moving the slider....")

print(minSlider.location,maxSlider.location)

act.drag_and_drop_by_offset(minSlider,100,0).perform()
act.drag_and_drop_by_offset(maxSlider,-100,0).perform()

print("locations After moving the slider....")

print(minSlider.location,maxSlider.location)

driver.close()