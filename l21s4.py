from selenium import webdriver
from selenium.webdriver.common.by import by
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    imput1.set_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()