#coding=utf-8
import unittest
import HTMLTestRunner
import time,os,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def sendmail(file_new):
	mail_from = '85202811@qq.com'
	mail_to = '120400665@qq.com'
	f = open(file_new,'rb')
	mail_body = f.read()
	f.close()
	msg = MIMEText(mail_body,'html','utf-8')
	msg['Subject'] = 'TEST REPORT'
	msg['From'] = '85202811@qq.com'
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
	result_report = 'C:\\Users\\lyancoffee\\Desktop\\testcase\\report'
	lists = os.listdir('C:\\Users\\lyancoffee\\Desktop\\testcase\\report')
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
	

	