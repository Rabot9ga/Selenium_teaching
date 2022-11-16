from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/selects1.html'
    browser.get(link)
    
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    summ = int(num1) + int(num2)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(summ))
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
    
    
