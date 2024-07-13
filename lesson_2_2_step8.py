from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Edge()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname('C:/Files'))    # получаем путь к директории текущего исполняемого файла 
print(current_dir)
file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
print(file_path)
own_file = browser.find_element(By.CSS_SELECTOR, "[type='file']")
own_file.send_keys(file_path)

input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
input1.send_keys("Игорь")
input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
input2.send_keys("Янковский")
input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
input3.send_keys("yiv1999@mail.ru")

#Нажать на кнопку Submit.
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(10)

