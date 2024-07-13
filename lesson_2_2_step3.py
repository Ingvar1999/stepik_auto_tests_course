from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Edge()
browser.get(link)

x1 = browser.find_element(By.ID, "num1")
n1 = int(x1.text)
x2 = browser.find_element(By.ID, "num2")
n2 = int(x2.text)
#print(x1)
#print(x2)
#print(n1)
#print(n2)
#print(n1+n2)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_visible_text(str(n1+n2))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()

#28.9634239882496
