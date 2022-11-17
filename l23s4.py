from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.ID, 'input_value').text
    y = math.log(abs(12*math.sin(int(x))))
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(y))
    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()
    
finally:
    time.sleep(5)
    browser.quit()


    
    
    
    
    
    