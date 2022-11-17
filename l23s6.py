from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()
    redir_page = browser.window_handles[1]
    browser.switch_to.window(redir_page)
    x = browser.find_element(By.ID, 'input_value').text
    y = math.log(abs(12*math.sin(int(x))))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(y))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()