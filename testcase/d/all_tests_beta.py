#coding=utf-8
import unittest
import HTMLTestRunner
import time
import unittest
import sys
sys.path.append('\\test_case')
from test_case import *


testunit = unittest.TestSuite()

testunit.addTest(unittest.makeSuite(wangpan.Login))
testunit.addTest(unittest.makeSuite(baidu.Baidu))
#runner = unittest.TextTestRunner()
#runner.run(testunit)

now = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime())
filename = 'C:\\Users\\zh\\Desktop\\testcase\\report\\'+now+'result2.html'
fp = file(filename,'wb')
	
runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp ,
	title = 'baiducase',
	description = 'result')
	
runner.run(testunit)