import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Edge()
browser.get(link)

#Нажать на кнопку Submit.
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
confirm = browser.switch_to.alert
confirm.accept()

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
print(y)

x_element = browser.find_element(By.ID, "answer")
x_element.send_keys(y)

#Нажать на кнопку Submit.
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
time.sleep(30)



