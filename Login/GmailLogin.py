import undetected_chromedriver as uc
import os
import time
import random


driver = uc.Chrome()
driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
	
	#login block
time.sleep(5)
	#add username in text
elem = driver.find_element_by_xpath('//*[@id="identifierId"]')
text = 'alex274@gmail.com'
for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
elem = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click
time.sleep(5)
elem = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
	#add password in text2

text2 = '#insertpass'
for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
print("Logged in!")
