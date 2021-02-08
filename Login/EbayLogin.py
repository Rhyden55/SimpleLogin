import undetected_chromedriver as uc
import os
import time
import random


driver = uc.Chrome()
driver.get('https://signin.ebay.com/')
	
	#login block
time.sleep(5)

	#add username in text
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="userid"]')
text = 'harry24@gmail.com'
for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="signin-continue-btn"]').click()
time.sleep(2)
elem = driver.find_element_by_xpath('//*[@id="pass"]')
	#add password in text2

text2 = '#insertpass'
for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="sgnBt"]').click()
print("Logged in!")
