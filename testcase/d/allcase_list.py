#coding=utf-8
import sys
sys.path.append('\\testcases')
from testcases import *

def caselist():
	alltestnames = [
		baidu.Baidu,
		wangpan.Login,
			]
		
	print "------success read case list!!!------"
	return alltestnames