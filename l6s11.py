from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
	link = 'http://suninjuly.github.io/registration1.html'
	browser = webdriver.Chrome()
	browser.get(link)
	input1 = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
	input1.send_keys('abc')
	input2 = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
	input2.send_keys('abc')
	input3 = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
	input3.send_keys('abc')
	input4 = browser.find_element(By.CSS_SELECTOR, ".second_block>.first_class>.first")
	input4.send_keys('abc')
	input5 = browser.find_element(By.CSS_SELECTOR, ".second_block>.second_class>.second")
	input5.send_keys('abc')
	submit = browser.find_element(By.CSS_SELECTOR, ".btn")
	submit.click()
	time.sleep(3)
	welcome = browser.find_element(By.TAG_NAME, 'h1')
	welcome_txt = welcome.text
	assert welcome_txt == "Congratulations! You have successfully registered!"

finally:
	time.sleep(10)
	browser.quit()