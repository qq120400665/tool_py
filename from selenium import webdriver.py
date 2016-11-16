from selenium.webdriver.chrome.options import Options
from selenium import webdriver

 


import time
op = Options()
op.add_argument('user-data-dir=C:\Users\lyancoffee\AppData\Local\Google\Chrome\User Data')
time.sleep(2)
dr = webdriver.Chrome(chrome_options=op)
time.sleep(2)
#dr = webdriver.Chrome()
#dr.get("http://baidu.com")

dr.save_screenshot(r'C:\\a.png')