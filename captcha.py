#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
from math import radians, cos, sin, asin, sqrt
import MySQLdb
from sshtunnel import SSHTunnelForwarder  
def get_captcha(phonenum):
	#db = MySQLdb.connect(host="115.29.208.235",user="dbadmin",passwd="dbadminpass",db="lyancafe",port=3306,charset="utf8")
	server = SSHTunnelForwarder(('114.55.141.208', 22),    
         ssh_password="zy123456",  
         ssh_username="zhaiy",  
         remote_bind_address=('rdsirbzrunuiayj.mysql.rds.aliyuncs.com', 3306)) 
	server.start()
	db = MySQLdb.connect(host='127.0.0.1',              
                           port=server.local_bind_port,  
                           user='lcread',  
                           passwd='Lc_2015_Read_0108',  
                           db='lyancafe')
	cursor = db.cursor()
	sql = "select captcha from t_user_captcha where login_name = " + phonenum
	try:
		cursor.execute(sql)
		captcha = cursor.fetchall()[-1]
		captcha = str(captcha)
		cursor.close()
		db.close()
		print type(captcha)
		print captcha[2:8]
		return captcha
	except Exception,e:
		return u'  未生成'

def clear_info():
	phone_num.set('')
	captcha.set('')

def set_captcha():
	phonenum = phone_num.get()
	captcha_ = get_captcha(phonenum)
	captcha.set(captcha_[2:8]) 	


root = Tk()
root.title("验证码查询")
#root.geometry('400x400')
root.geometry('210x80')
#l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2).pack()

Label(root, text="手机号码").grid(row=0)
Label(root, text="验证码").grid(row=1)

phone_num = StringVar()
e1 = Entry(root,text = phone_num)
captcha = StringVar()
e2 = Entry(root,text = captcha)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#photo = PhotoImage(file='.\\690e2a0828381f3056038f33a8014c086e06f030.gif')
#label = Label(image=photo)
#label.image = photo
#label.grid(row=0, column=4, columnspan=4, rowspan=4, sticky=W+E+N+S, padx=5, pady=5)


#label['textvariable'] = display
#Button(root, text = 'C', fg = '#EF7321', width = 3, command = lambda: clear()).grid(row = 1, column = 0,columnspan=2)

Button(root, text="   查询   ", command = set_captcha).grid(row=2,column=0)
Button(root, text="   复位   ", command = clear_info).grid(row=2,column=1)

root.mainloop()
#print haversine(116.489195,39.996912,116.480486,40.004802224)