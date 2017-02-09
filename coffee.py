#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import HTMLTestRunner
i = 0 
while i < 50:
	dr = webdriver.Chrome()
	dr.get('http://mtest.lyancafe.com/test/mock?token=ilovetest')
	dr.find_element_by_id('newbuyBtn').click()
	time.sleep(1)
	dr.find_element_by_class_name('choose-brand').click()
	time.sleep(1)
	dr.find_elements_by_class_name('add-icon')[10].click()
	time.sleep(1)
	dr.find_elements_by_class_name('add-icon')[10].click()
	time.sleep(1)
	'''dr.find_element_by_class_name('add-icon').click()
	time.sleep(2)
	dr.find_element_by_class_name('add-icon').click()
	time.sleep(2)
	dr.find_element_by_class_name('add-icon').click()
	time.sleep(2)
	dr.find_element_by_class_name('add-icon').click()
	time.sleep(2)
	dr.find_element_by_class_name('add-icon').click()
	time.sleep(2)
	dr.find_element_by_class_name('add-icon').click()
	time.sleep(2)
	dr.find_element_by_class_name('add-icon').click()
	time.sleep(2)'''
	dr.find_element_by_class_name('btn').click()
	time.sleep(1)
	dr.find_element_by_class_name('js-exp-time').click()
	time.sleep(1)
	dr.find_elements_by_class_name('dayinfo')[0].click()
	time.sleep(1)
	dr.find_elements_by_class_name('slottitle')[1].click()
	time.sleep(1)
	dr.find_element_by_class_name('js-confirm').click()
	time.sleep(1)
	dr.find_element_by_class_name('confirm-btn').click()
	time.sleep(2)
	#dr.find_elements_by_class_name('radio-img')[1].click()
	#time.sleep(1)
	#dr.find_element_by_id("select-date").find_elements_by_tag_name("option")[1].click();
	#time.sleep(1)
	#dr.find_element_by_class_name('btn').click()
	#time.sleep(1)
	dr.quit()
	print i 
	i = i+1

