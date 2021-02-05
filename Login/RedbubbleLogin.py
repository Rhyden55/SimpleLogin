import undetected_chromedriver as uc
import os
import time
import random

driver = uc.Chrome()
driver.get('https://redbubble.com/auth/login/')
	
	#login block
elem = driver.find_element_by_xpath('//*[@id="ReduxFormInput1"]')
	#add username in text

text = '#insert email'

for character in text:
	elem.send_keys(character)	
	time.sleep(0.3)
elem = driver.find_element_by_xpath('//*[@id="ReduxFormInput2"]')
	#add password in text2

text2 = '#insert pass'

for character in text2:
	elem.send_keys(character)	
	time.sleep(0.3)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="RB_React_Component_LoginFormContainer_0"]/div/form/span/button').click()
print("Logged in!")

