#coding=utf-8
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header

sender = '85202811@qq.com'

receiver = '120400665@qq.com'

subject = 'python email test'

smtpserver = 'smtp.qq.com'

username = '85202811@qq.com'
password = 'zhaiyuan2007'

msg = MIMEText('<html><h1>HALO!</h1><html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
time.sleep(2)
#smtp.esmtp_features["auth"]="LOGIN PLAIN"
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()