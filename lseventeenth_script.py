from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time 
def calc(x):
 return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/get_attribute.html")
button1 = browser.find_element(By.ID, 'treasure')
x = button1.get_attribute("valuex")
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = browser.find_element(By.ID, "robotsRule")
option2.click()
button2 = browser.find_element(By.CSS_SELECTOR, ".btn")
button2.click()

time.sleep(30)
browser.quit()