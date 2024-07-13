import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Edge()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
#print(y)
#time.sleep(10)

x_element = browser.find_element(By.ID, "answer")
x_element.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, "[class='form-check-input']")
option1.click()

option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option1.click()
time.sleep(14)
#Нажать на кнопку Submit.

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

