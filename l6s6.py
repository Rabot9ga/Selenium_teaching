from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elemenents = browser.find_elements(By.TAG_NAME, 'input')
    for elemenent in elemenents:
        elemenent.send_keys('abcd')

    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
