from selenium import webdriver
import time
dr = webdriver.Chrome()
dr.get('http://mxd2.qq.com/cp/a20170205mxd/index.htm')
dr.find_element_by_id('dologin').click()
dr.switch_to_frame('loginIframe')
dr.find_element_by_id('switcher_plogin').click()
dr.find_element_by_id('u').send_keys('120400665')
dr.find_element_by_id('p').send_keys('qq120400665QQ')
dr.find_element_by_id('login_button').click()
dr.switch_to_default_content()
dr.find_element_by_class_name('btn_mf').click()
time.sleep(1)
dr.close()