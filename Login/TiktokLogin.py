import undetected_chromedriver as uc
import os
import time
import random


driver = uc.Chrome()
driver.get('https://www.tiktok.com/login/phone-or-email/email')
	
	#login block
time.sleep(5)

	#add username in text
time.sleep(5)
elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[2]/div/input')
text = 'insertemail'
for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[3]/div/input')
	#add password in text2

text2 = '#insertpass'
for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/button').click()
print("Logged in!")