import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Edge()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#button = browser.find_element(By.ID, "book")
#button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "book")))
#button = WebDriverWait(browser, 20).text_to_be_present_in_element((By.ID, "price"), "$100")
button = browser.find_element(By.ID, "book")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
print(x)
y = calc(x)
print(y)

x_element = browser.find_element(By.ID, "answer")
x_element.send_keys(y)

#Нажать на кнопку Submit.
button = browser.find_element(By.ID, "solve")
button.click()
time.sleep(30)
#29.052438197286985

