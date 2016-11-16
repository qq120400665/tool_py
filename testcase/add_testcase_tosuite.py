#coding=utf-8
import unittest
import HTMLTestRunner
import time,os,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
listaa = 'C:\\Users\\lyancoffee\\Desktop\\py\\testcase\\testcases'
def creatsuite():	
	testunit = unittest.TestSuite()
	loader_discover = unittest.defaultTestLoader.discover(listaa, pattern='start_*.py', top_level_dir=None)
	discover = loader_discover
	
	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTests(test_case)
			print test_suite
	return testunit
alltestnames = creatsuite()
report = os.listdir(r'C:\\Users\\lyancoffee\\Desktop\\py\\testcase\\report')
report_num = len(report)
now = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime())
filename = 'C:\\Users\\lyancoffee\\Desktop\\py\\testcase\\report\\'+now+'&'+str(report_num+1)+'.html'
fp = file(filename,'wb')
	
runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp ,
	title = 'baiducase',
	description = 'result')
runner.run(alltestnames)