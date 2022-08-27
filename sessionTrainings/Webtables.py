from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')

#no of rows in a table
noOfrows=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
print(len(noOfrows))

#no of columns
noOfColumns=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th")
print(len(noOfColumns))

# Read specific row and column data(reading 5th row and 1st column data
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]")
print(data.text)

# Read all the row and coloumns data:
for row in range(2,len(noOfrows)+1):
    for column in range(1,len(noOfColumns)+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(column)+"]")
        print(data.text,end='   ')
    print()

#Read data based on condition:
for row in range(2,len(noOfrows)+1):
        authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
        if authorname=='Mukesh':
            bookname=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[1]").text
            print("bookname: ", bookname)





driver.close()