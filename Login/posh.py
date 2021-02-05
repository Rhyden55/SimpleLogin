import undetected_chromedriver as uc
import os
import time
import random


driver = uc.Chrome()
driver.get('https://poshmark.com/login')
	
	#login block
elem = driver.find_element_by_id('login_form_username_email')
	#add username in text

text = '#insert email'
for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
elem = driver.find_element_by_id('login_form_password')
	#add password in text2

text2 = '#insert pass'
for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
driver.find_element_by_xpath("//button[@class='btn blue btn-primary']").click()
print("Logged in!")
