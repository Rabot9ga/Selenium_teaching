from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os 


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('abc')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('abc')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('abc')
    send_file = browser.find_element(By.NAME, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt') 
    send_file.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
    
    
