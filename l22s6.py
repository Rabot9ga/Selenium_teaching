from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/execute_script.html'
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(y))
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
    
