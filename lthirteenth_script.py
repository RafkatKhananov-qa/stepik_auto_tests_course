from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

try:
 browser = webdriver.Chrome()
 browser.get('http://suninjuly.github.io/file_input.html')
 input1 = browser.find_element(By.CSS_SELECTOR, ".form-group > input:nth-child(2)")
 input1.send_keys("Rafkat")
 input2 = browser.find_element(By.CSS_SELECTOR, ".form-group > input:nth-child(4)")
 input2.send_keys("Khananov")
 input3 = browser.find_element(By.CSS_SELECTOR, ".form-group > input:nth-child(6)")
 input3.send_keys("raf@mail.ru")
 current_dir = os.path.abspath(os.path.abspath('/Users/Rafkat/Desktop/Python + Selenium + Allure/selenium_course/'))
 file_path = os.path.join(current_dir, 'name.txt')
 element = browser.find_element(By.NAME, "file")
 element.send_keys(file_path)
 browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
 time.sleep(30)
 browser.quit()
