import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Edge()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x1 = browser.find_element(By.ID, "input_value")
n1 = int(x1.text)
print(x1)
#print(x2)
print(n1)
#print(n2)
#print(n1+n2)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
#print(y)
#time.sleep(10)

x_element = browser.find_element(By.ID, "answer")
x_element.send_keys(y)

browser.execute_script("window.scrollBy(0, 300);")

option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

option1 = browser.find_element(By.ID, "robotsRule")
option1.click()
#time.sleep(14)
#Нажать на кнопку Submit.

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

