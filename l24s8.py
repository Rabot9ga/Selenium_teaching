from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)
    button1 = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button1.click()
    x = browser.find_element(By.ID, 'input_value').text
    y = math.log(abs(12*math.sin(int(x))))
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys(str(y))
    button2 = browser.find_element(By.ID, 'solve')
    button2.click()
    
finally:
    time.sleep(5)
    browser.quit()
    