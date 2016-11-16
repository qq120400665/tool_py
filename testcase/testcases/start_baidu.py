#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
import HTMLTestRunner

class Baidu(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.baidu.com/"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_baidu(self):
		u'''百度搜索'''
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("kw").send_keys('selenium wendriver')
		driver.find_element_by_id("su").click()
		time.sleep(2)
		driver.close()
		
	def test_baidu_set(self):
		u'''百度设置'''
		driver = self.driver
		driver.get(self.base_url)
		#m = driver.find_element_by_class_name("pf")
		#ActionChains(driver).move_to_element(m).perform()
		driver.find_element_by_xpath("//div[@id='u1']/a[7]").click()
		driver.find_element_by_xpath("//div[@class='bdpfmenu']/a[2]").click()
		
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()
	#testunit = unittest.TestSuite()
	
	#testunit.addTest(Baidu("test_baidu"))
	#testunit.addTest(Baidu("test_baidu_set"))
	
	#filename = 'C:\\Users\\zh\\Desktop\\testcase\\report\\result.html'
	#fp = file(filename,'wb')
	
	#runner = HTMLTestRunner.HTMLTestRunner(
	#stream = fp ,
	#title = 'baiducase',
	#description = 'result')
	
	#runner.run(testunit)