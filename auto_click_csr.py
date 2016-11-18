#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib
import re
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import json
class AUTOCLICK:

    def __init__(self):
        op = Options()
        op.add_argument('user-data-dir=C:\Users\lyancoffee\AppData\Local\Google\Chrome\User Data')
        #self.dr = webdriver.Chrome(chrome_options=op)
        self.dr = webdriver.Chrome()
        self.link_list = []
        self.link_list_name = []
        self.link_pass = []
        self.link_fail = []

    def element_exist(self,ele):
        '''check element exist or not by tag name'''
        try:
            self.dr.find_element_by_tag_name(ele)
            return True
        except Exception,e:
            return False

    def find_eachlink(self):
        self.dr.get('http://op.lyancafe.com/csr/home')
        time.sleep(1)
        self.dr.find_element_by_id('loginName').send_keys('zhaiyuan')
        self.dr.find_element_by_id('password').send_keys('lyan2014')
        self.dr.find_element_by_class_name('btn').click()
        time.sleep(3)
        self.link_object = self.dr.find_elements_by_tag_name('a')
        for i in self.link_object:
            self.link_list.append(i.get_attribute('href'))
            self.link_list_name.append(i.text)
        self.link_list.remove('http://op.lyancafe.com/csr/logout')
        #self.link_list.remove('')
        #self.link_list_name.remove(u'閫�鍑虹郴缁�')
        #self.link_list_name.remove(u'缁撶畻绠＄悊')
        #self.link_list.remove('')
        print self.link_list
        print len(self.link_list)
        #print self.link_list_name
        print 'link_list_name:',json.dumps(self.link_list_name, encoding='UTF-8', ensure_ascii=False)
        print len(self.link_list_name)
        return self.link_list

    def click_eachlink(self):
        self.link_list = self.find_eachlink()
        n = 1
        for i in self.link_list:
            '''print n,'now connecting',i,'............'
            self.dr.get(i)
            n = n+1'''
            try:
                self.dr.get(i)
                if self.dr.find_element_by_tag_name('title') != 'Apache Tomcat/7.0.54 - Error report' and self.element_exist('h2') is False:
                    print n,'now conneting',i,'....PASS'
                    self.link_pass.append(i)
                else:
                    print n,'now conneting',i,'....PAGE ERROR'
                    self.link_fail.append(i)
                n = n + 1
            except Exception,e:
                print Exception,':',e
                print 'wrongs!!!'
                continue
            time.sleep(2)
        print 'finish,failed page as follows:',self.link_fail

    def getHtml(self,url):
        page = urllib.urlopen(url)
        html = page.read()
        return html

#涓嬭浇椤甸潰鍥剧墖
    def cbk(a, b, c):

        '''鍥炶皟鍑芥暟

        @a: 宸茬粡涓嬭浇鐨勬暟鎹潡

        @b: 鏁版嵁鍧楃殑澶у皬

        @c: 杩滅▼鏂囦欢鐨勫ぇ灏�

        '''

        per = 100.0 * a * b / c
        if per > 100:

            per = 100

        print '%.2f%%' % per

    def getImg(self,html):
        reg = r'<a herf="\/.">'   #<a href="/csr/giftcardrefundaudit/customermanager">璇蜂汉鍠濋��娆句竴绾у鏍�</a>
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        if imglist:
            for i in imglist:
                print i
        else:
            print 'XXXXXXX'
        #x = 0
        #for imgurl in imglist:
            #urllib.urlretrieve(imgurl,'%s.gif' % x,cbk)
            #print '-------now save %s ---------' % x
            #x+=1

    def getjpg(self,html):
        reg = r'src="(http://.+?\.jpg)"'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        x = 100
        for imgurl in imglist:
            urllib.urlretrieve(imgurl,'%s.gif' % x,cbk)
            print '-------now save %s ---------' % x
            x+=1
#url = 'http://optest.lyancafe.com/csr/home'
a = AUTOCLICK()
a.click_eachlink()
#html = a.getHtml(url)
#print html
#a.getImg(html)
##print getjpg(html)

# from selenium import webdriver
# dr = webdriver.Chrome()
# try:
#     dr.get(123)
# finally:
#     print 123