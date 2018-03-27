






from selenium import webdriver
from selenium.webdriver import ActionChains

import time
from time import sleep
import os


driver=webdriver.Firefox()
driver.delete_all_cookies()
driver.get('https://topface.com')
driver.maximize_window()
print('driver opened')
sleep(7)

klasse='/html/body/div[2]/div[2]/div/div[5]/a[2]/div[3]/table/tbody/tr/td'
elem=driver.find_element_by_xpath(klasse)
ActionChains(driver).move_to_element(elem).click().perform()
print('login clicked')
sleep(5)

driver.switch_to_window(driver.window_handles[1])
sleep(5)
print('window switched')

elem=driver.find_element_by_id('email').send_keys('username')
elem=driver.find_element_by_id('pass').send_keys('password')
sleep(3)
elem=driver.find_element_by_id('loginbutton').click()
print('got it')

sleep(4)
driver.switch_to_window(driver.window_handles[0])
print('window switched 2')

driver.refresh()

sleep(2)

klasse='/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div/div[2]'
elem=driver.find_element_by_xpath(klasse)
ActionChains(driver).move_to_element(elem).click().perform()
sleep(2)
driver.refresh()

print('refresh 2')
n=0
while True:
	sleep(10)
	n=n+1
	klasse='/html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[3]/div[1]/div[2]/a[3]/div'
	elem=driver.find_element_by_xpath(klasse)
	ActionChains(driver).move_to_element(elem).click().perform()
	print('chick liked',n)
	sleep(2)

print('end')
