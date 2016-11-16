#coding=utf-8
import unittest
import HTMLTestRunner
import time,os,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#import sys
#sys.path.append('\\testcases')
#from testcases import *
#import allcase_list
#alltestnames = allcase_list.caselist()
#for test in alltestnames:
	#testunit.addTest(unittest.makeSuite(test))
#runner = unittest.TextTestRunner()
#runner.run(testunit)
listaa = 'C:\\Users\\zh\\Desktop\\testcase'
def creatsuite():	
	testunit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(listaa,
	pattern = 'start_*.py',
	top_level_dir = None)
	
	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTests(test_case)
			print test_suite
	return testunit
alltestnames = creatsuite()
report = os.listdir(r'C:\\Users\\zh\\Desktop\\testcase\\report')
report_num = len(report)
now = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime())
filename = 'C:\\Users\\zh\\Desktop\\testcase\\report\\'+now+'&'+str(report_num+1)+'.html'
fp = file(filename,'wb')
	
runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp ,
	title = 'baiducase',
	description = 'result')
	
#runner.run(alltestnames)
def sendmail(file_new):
	mail_from = '85202811@qq.com'
	mail_to = '120400665@qq.com'
	f = open(file_new,'rb')
	mail_body = f.read()
	f.close()
	msg = MIMEText(mail_body,'html','utf-8')
	msg['Subject'] = u'测试报告'
	msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
	smtp = smtplib.SMTP()
	smtp.connect('smtp.qq.com')
	smtp.login('85202811@qq.com','zhaiyuan2007')
	smtp.sendmail(mail_from,mail_to,msg.as_string())
	smtp.quit()
	print 'email has send out!'
	
def sendreport():
	lists1 =[]
	lists2 = []
	a = ''
	result_report = 'C:\\Users\\zh\\Desktop\\testcase\\report'
	lists = os.listdir('C:\\Users\\zh\\Desktop\\testcase\\report')
	for i in lists:
		lists1.append(i.split('&')[1])
	for i in lists1:
		lists2.append(i.split('.html')[0])
	print lists
	print lists1
	print lists2
	b = '&'+str(lists2[-1])+'.html'
	for i in lists:
		if b in i:
			print i
			a = i
	print 'the new report:'+a
	file_new = os.path.join(result_report,a)
	print file_new
	sendmail(file_new)
	
if __name__ =='__main__':
	runner.run(alltestnames)
	sendreport()
		