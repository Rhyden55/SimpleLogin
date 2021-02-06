import undetected_chromedriver as uc
import os
import time
import random

driver = uc.Chrome()
driver.get('https://www.pinterest.com/login')
	
	#login block
elem = driver.find_element_by_xpath('//*[@id="email"]')
	#add username in text

text = '#insert email'

for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
elem = driver.find_element_by_xpath('//*[@id="password"]')
	#add password in text2

text2 = '#insert pass'

for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div[3]/div/div/div[3]/form/div[5]/button/div').click()
print("Logged in!")
