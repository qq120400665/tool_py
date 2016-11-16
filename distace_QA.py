#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
from math import radians, cos, sin, asin, sqrt
import MySQLdb
from sshtunnel import SSHTunnelForwarder  
def get_orderinfo(orderid):
	#db = MySQLdb.connect(host="115.29.208.235",user="dbadmin",passwd="dbadminpass",db="lyancafe",port=3306,charset="utf8")
	server = SSHTunnelForwarder(('115.29.208.235', 22),    
         ssh_password="lyan2014",  
         ssh_username="zhaiy",  
         remote_bind_address=('115.29.208.235', 3306)) 
	server.start()
	db = MySQLdb.connect(host='127.0.0.1',              
                           port=server.local_bind_port,  
                           user='dbadmin',  
                           passwd='dbadminpass',  
                           db='lyancafe')
	cursor = db.cursor()
	sql1 = "select shop_id,customer_address_id from orders where id = " + orderid
	cursor.execute(sql1)
	shop_id,customer_address_id = cursor.fetchone()
	customer_address_id = str(customer_address_id)
	shop_id = str(shop_id)
	sql2 = "select lng,lat from t_shop where id = " + shop_id
	cursor.execute(sql2)
	lng,lat = cursor.fetchone()
	lng = float(lng)
	lat = float(lat)
	sql3 = "select lng,lat from customer_address where id = " + customer_address_id
	cursor.execute(sql3)
	lng1,lat1 = cursor.fetchone()
	cursor.close()
	db.close()


	#print shop_id,customer_address_id,lng,lat,lng1,lat1
	print shop_id,customer_address_id,lng,lat,lng1,lat1
	return lng,lat,lng1,lat1
	
def haversine():
	orderid = order_id.get()
	#lon1,lat1,lon2,lat2 = 116.489195,39.996912,116.480486,40.004804
	
	lon1,lat1,lon2,lat2 = get_orderinfo(orderid)
	print lat1,lon1,lat2,lon2
	location_shop_ = str(lat1) + ',' + str(lon1)
	location_customer_ = str(lat2) + ',' + str(lon2)
	location_shop.set(location_shop_)
	location_customer.set(location_customer_)	
	lon1,lat1,lon2,lat2 = map(radians,[lon1,lat1,lon2,lat2])
	
	
	print type(lat1)
	print type(lon1)
	print type(lon2)
	print type(lat2)
	print lon1,lat1,lon2,lat2
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
	c = 2 * asin(sqrt(a))  
	r = 6371
	#print c*r*1000
	distance_ = c*r
	distance.set(distance_)
	print distance_
	if distance_>0 and distance_<1.5:
		salary.set(0)
		return 0,distance_
	elif distance_>1.5 and distance_ < 2.0:
		salary.set(1)
		return 1,distance_
	elif distance_>2.0 and distance_ < 2.5:
		salary.set(2)
		return 2,distance_
	elif distance_>2.5 and distance_ < 3.0:
		salary.set(3)
		return 3,distance_
	elif distance_>3.0 and distance_ < 3.5:
		salary.set(4)
		return 4,distance_
	elif distance_>3.5:
		salary.set(5)
		return 5,distance_
	else:
		salary.set("wrong")
		return 'wrong distance',distance_

def clear_info():
	order_id.set('')
	location_shop.set('')
	location_customer.set('')
	distance.set('')
	salary.set('')

root = Tk()
root.title("caculate distance")
#root.geometry('400x400')
root.geometry('420x210')
#l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2).pack()

Label(root, text="order_id").grid(row=0)
Label(root, text="location_shop").grid(row=1)
Label(root, text="location_customer").grid(row=2)
Label(root, text="distance(km)").grid(row=3)
Label(root, text="salary").grid(row=4)

order_id = StringVar()
e1 = Entry(root,text = order_id)
location_shop = StringVar()
e2 = Entry(root,text = location_shop)
location_customer = StringVar()
e3 = Entry(root,text = location_customer)
distance = StringVar()
e4 = Entry(root,text = distance)
salary = StringVar()
e5 = Entry(root,text = salary)




e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)


photo = PhotoImage(file='.\\690e2a0828381f3056038f33a8014c086e06f030.gif')
label = Label(image=photo)
label.image = photo
label.grid(row=0, column=4, columnspan=4, rowspan=4, sticky=W+E+N+S, padx=5, pady=5)


#label['textvariable'] = display
#Button(root, text = 'C', fg = '#EF7321', width = 3, command = lambda: clear()).grid(row = 1, column = 0,columnspan=2)

Button(root, text="caculate", command = haversine).grid(row=4,column=5)
Button(root, text="   clear   ", command = clear_info).grid(row=4,column=6)

root.mainloop()
#print haversine(116.489195,39.996912,116.480486,40.004804)