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
        self.link_wrong = []

    def element_exist(self,ele):
        '''check element exist or not by tag name'''
        try:
            self.dr.find_element_by_tag_name(ele)
            return True
        except Exception,e:
            return False

    def find_eachlink(self,url):
        self.dr.get(url)
        time.sleep(1)
        self.dr.find_element_by_id('loginName').send_keys('zhaiyuan')
        self.dr.find_element_by_id('password').send_keys('lyan2014')
        self.dr.find_element_by_class_name('btn').click()
        time.sleep(3)
        self.link_object = self.dr.find_elements_by_tag_name('a')
        print self.link_object
        for i in self.link_object:
            if i.get_attribute('href') is not None:
                self.link_list.append(i.get_attribute('href'))
                self.link_list_name.append(i.text)
        self.link_list.remove(url[:-4]+'logout')
        #self.link_list.remove('')
        self.link_list_name.remove(u'退出系统')
        print self.link_list
        for i in self.link_list:
            print i
        print len(self.link_list)
        print 'link_list_name:',json.dumps(self.link_list_name, encoding='UTF-8', ensure_ascii=False)
        print len(self.link_list_name)
        return self.link_list,self.link_list_name

    def click_eachlink(self):
        (self.link_list,self.link_list_name) = self.find_eachlink(url)
        n = 1
        for i in range(0,len(self.link_list)):
            '''print n,'now connecting',i,'............'
            self.dr.get(i)
            n = n+1'''
            try:
                self.dr.get(str(self.link_list[i]))
                print self.dr.find_element_by_tag_name('title').get_attribute('innerHTML')
                if self.dr.find_element_by_tag_name('title').get_attribute('innerHTML') != 'Apache Tomcat/7.0.54 - Error report' and self.element_exist('h2') is False:
                    print n,'now conneting',self.link_list[i],'....PASS'
                    self.link_pass.append(self.link_list_name[i])
                    n+=1
                else:
                    print n,'now conneting',self.link_list[i],'....FAIL'
                    self.link_fail.append(self.link_list_name[i])
                    n+=1
            except Exception,e:
                print n,Exception,':',e
                self.link_wrong.append(self.link_list_name[i])
                print 'wrongs!!!'
                continue
                n+=1
                time.sleep(2)
        print 'finish,failed pages as follows:',json.dumps(self.link_fail,encoding='UTF-8',ensure_ascii=False)
        print 'finish,wrong pages as follows:',json.dumps(self.link_wrong,encoding='UTF-8',ensure_ascii=False)

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
url = 'http://op.lyancafe.com/csr/home'
print url[:-4]+'logout'
a = AUTOCLICK()
a.click_eachlink()

# from selenium import webdriver
# dr = webdriver.Chrome()
# try:
#     dr.get(123)
# finally:
#     print 123
