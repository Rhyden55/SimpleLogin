import undetected_chromedriver as uc
import os
import time
import random


driver = uc.Chrome()
driver.get('https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fwelcome')
	
	#login block
time.sleep(5)

	#add username in text
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="username"]')
text = 'insertemail'
for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
elem = driver.find_element_by_xpath('//*[@id="password"]')
	#add password in text2

text2 = '#insertpass'
for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/div/div/div[3]/article/div[1]/div/form/div[4]/button').click()
print("Logged in!")
