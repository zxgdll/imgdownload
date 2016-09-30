#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import re
import requests
#
# url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1475208601259_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E4%BA%8E%E6%B9%89'

url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1475210618276_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%86%8A'
request=urllib2.Request(url)
pattern=u'\"objURL\":\"(.*?)\"'
response=urllib2.urlopen(request)
page=response.read()
x=0
try:
	items=re.findall(pattern,page,re.S)
	print(len(items))
	for item in items:
		try:
			pic=requests.get(item,timeout=30)
		except requests.exceptions.ConnectionError:
			print('[ERROR] image is not downloaded!')
			continue
		string='pictest/'+str(x)+'.jpg'
		f=open(string,'wb')
		f.write(pic.content)
		f.close()
		x+=1
except urllib2.URLError,e:
	if hasattr(e,"reason"):
		print(e.reason)
	if hasattr(e,"code"):
		print(e.code)
