#!/usr/bin/env python
#coding=utf-8
import re
import urllib
class img:
	def getPage(self,url):
		page=urllib.urlopen(url)
		response=page.read()
		return response
	def getimg(sels,str_word,page):
		pattern=u'\"objURL\":\"(.*?)\"'
		items=re.findall(pattern,page,re.S)
		print(len(items))
		i=0
		for item in items:
			string='pic/'+str_word+str(i)+'.1.jpg'
			#urllib.urlretrieve 只能读取65464字节以下的文件
			pic=urllib.urlretrieve(item,string)
			i+=1

spider=img()
flag=True
while flag:
	input=raw_input('输入你想要的表情包(Q结束)：')
	if input=='Q':
		flag=False
		break
	url='http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='+str(input)
	page1=spider.getPage(url)
	spider.getimg(str(input),page1)
	print('下载结束！')