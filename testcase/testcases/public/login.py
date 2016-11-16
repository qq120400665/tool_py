#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
#登陆模块（函数）
def login(self):
	driver = self.driver
	driver.maximize_window()
	driver.find_element_by_id("TANGRAM__PSP_4__userName").clear()
	driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(u"悠闲纷飞")
	driver.find_element_by_id("TANGRAM__PSP_4__password").clear()
	driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("zhaiyuan2007")
	driver.find_element_by_id("TANGRAM__PSP_4__submit").click()
	time.sleep(3)		
	driver.find_element_by_id("_disk_id_12").click()