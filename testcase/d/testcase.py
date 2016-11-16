#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time
import login

class Login(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://pan.baidu.com"
		self.verificationErrors = []
		self.accept_next_alert = True
		

	def test_login(self):
		driver = self.driver
		driver.get(self.base_url)
		driver.maximize_window()
		login.login(self)
		#driver.find_element_by_id("TANGRAM__PSP_4__userName").clear()
		#driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys(u"悠闲纷飞")
		#driver.find_element_by_id("TANGRAM__PSP_4__password").clear()
		#driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("zhaiyuan2007")
		#driver.find_element_by_id("TANGRAM__PSP_4__submit").click()
		time.sleep(2)
		#driver.find_element_by_id("_disk_id_12").click()

		quit = driver.find_element_by_class_name("top-username")
		ActionChains(driver).move_to_element(quit).perform()
		time.sleep(2)
		driver.find_element_by_class_name("j-logout").click()
		time.sleep(2)
		driver.find_element_by_id('_disk_id_28').click()
		
	def tearDown(self):
		#self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()