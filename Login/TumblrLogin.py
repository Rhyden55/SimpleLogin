import undetected_chromedriver as uc
import os
import time
import random


driver = uc.Chrome()
driver.get('https://www.tumblr.com/login')
	
	#login block
time.sleep(5)

	#add username in text
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="signup_determine_email"]')
text = 'chill389@gmail.com'
for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(2)
elem = driver.find_element_by_xpath('//*[@id="signup_forms_submit"]/span[2]').click()
time.sleep(2)
elem = driver.find_element_by_xpath('//*[@id="signup_magiclink"]/div[2]').click()
time.sleep(2)
elem = driver.find_element_by_xpath('//*[@id="signup_password"]')	
	#add password in text2

text2 = '#insertpass'
for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/button[1]/span[6]').click()
print("Logged in!")
