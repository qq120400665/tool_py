# import hashlib
import time
# params=[]
# nonce = 'nonce='+str(time.time()).split('.')[0]+'000'
# appid = 'appid=dbc1e0a09f15cac4cabf38ed5c0d5974'
# appkey = 'appkey=7e5c0e6a82e026588f4abf02260fa7c3'
# params.append(nonce)
# params.append(appid)
# params.sort()
# params.append(appkey)
# sign_ex = '&'.join(params)
# sign = hashlib.sha1(sign_ex).hexdigest()
# print 'sign:',sign
# print 'nonce:',str(time.time()).split('.')[0]+'000'
# print 'appid:dbc1e0a09f15cac4cabf38ed5c0d5974'
name1={'app_qusong':['e2beb30fe93cd5ca9ed0ba705a4e6096','4252855545bfabcf39a7d7d2ea7e268b9925d81e']}

name2= {'app_wokuaidao':['9c838579adda7f729382e226459340e3','7fd154b4fa0afa268f607dde2c381703aa108c21']}
# n=1
# m = 1
# params_withsign = []
nonce = str(time.time()).split('.')[0]+'000'
# caselists_params = {}
# for name in names:
# 	params = {}
# 	print 'name.values()[0][0]:',name.values()[0][0]
# 	caselists_params['appid'] = name.values()[0][0]
# 	caselists_params['nonce'] = nonce
# 	caselists_params['test'] = m
# 	print 'caselists_params[i]',caselists_params
# 	print 'name.keys():',name.keys()
# 	params['caselists_params_'+str(name.keys())+'_'+str(n)] = caselists_params
# 	print 'params:',params
# 	params_withsign.append(params)
# 	print 'params_withsign',params_withsign
# 	m+=1
# n=1
# caselists_params = {}
# params = {}
# params_withsign=[]
# print 'name1.values()[0][0]1:',name1.values()[0][0]
# caselists_params['appid'] = name1.values()[0][0]
# caselists_params['nonce'] = nonce
# print 'caselists_params[i]1',caselists_params
# print 'name.keys()1:',name1.keys()
# params['caselists_params_1'+str(name1.keys())+'_'+str(n)] = caselists_params
# print 'params1:',params
# params_withsign.append(params)
# print 'params_withsign1',params_withsign


# params1 = {}
# print 'params_withsign2',params_withsign
# print 'name2.values()[0][0]2:',name2.values()[0][0]
# print 'params_withsign3',params_withsign
# caselists_params['appid'] = name2.values()[0][0]
# print 'params_withsign4',params_withsign
# caselists_params['nonce'] = nonce
# print 'params_withsign5',params_withsign
# print 'caselists_params[i]2',caselists_params
# print 'params_withsign6',params_withsign
# print 'name.keys():2',name2.keys()
# print 'params_withsign7',params_withsign
# params1['caselists_params_2'+str(name2.keys())+'_'+str(n)] = caselists_params
# print 'params_withsign8',params_withsign
# print 'params1:',params1
# print 'params_withsign9',params_withsign
# params_withsign.append(params1)
# print 'params_withsign',params_withsign
# names = [10,20,30]
# alice = {}
# bruce = []
# for name in names:
# 	color = {}
# 	alice = {}
# 	alice['old'] =name
# 	print 'alice:',alice
# 	color['info'] = alice
# 	print 'color:',color
# 	bruce.append(color)
# 	print 'bruce:',bruce

class tt():
	def rr(self,a,b):
		return a+b
	def cc(self):
		c = self.rr(a,b)
		print c
	def dd(self):
		d = self.dd()
a = 1
b = 2
if __name__ == '__main__':
	t = tt()
	t.cc()


















