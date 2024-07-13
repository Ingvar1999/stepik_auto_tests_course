import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Edge()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Нажать на кнопку Alert.

button = browser.find_element(By.CLASS_NAME, "trollface")
button.click()

browser.switch_to.window(browser.window_handles[1])

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
print(y)

x_element = browser.find_element(By.ID, "answer")
x_element.send_keys(y)
#time.sleep(30)

#Нажать на кнопку Submit.
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
time.sleep(30)



