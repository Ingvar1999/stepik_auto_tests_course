
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Edge()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

x_element = browser.find_element(By.ID, "answer")
x_element.send_keys(y)
option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
option1.click()

option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
option1.click()

browser.execute_script("window.scrollBy(0, 150);")
#Нажать на кнопку Submit.

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()


Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

 

Когда ваш код заработает, попробуйте запустить его на странице https://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.
