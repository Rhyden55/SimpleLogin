import undetected_chromedriver as uc
import os
import time
import random

driver = uc.Chrome()
driver.get('https://twitter.com/login')
	
	#login block
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
	#add username in text

text = '#insert email'

for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
elem = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
	#add password in text2

text2 = '#insert pass'

for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
print("Logged in!")

