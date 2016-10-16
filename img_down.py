#!/usr/bin/env python
#coding=utf-8
import urllib2
import requests
import re
import os
class image:
	def getPage(self,url):
		request=urllib2.Request(url)
		response=urllib2.urlopen(request)
		page=response.read()
		return page
	def imgDown(self,input,str_word,page):
		pattern=u'\"objURL\":\"(.*?)\"'
		items=re.findall(pattern,page,re.S)
		x=0
		print(len(items))
		newpath=os.path.join('pics/',input) #为表情包创建独立的文件夹
		# print(newpath)
		os.mkdir(newpath)
		for item in items:
			try:
				pic=requests.get(item,timeout=50)
			except requests.exceptions.ConnectionError:
				print('[错误]：下载失败')
				continue
			picstr=newpath+'/'+str_word[:len(input)]+str(x)+'.jpg'
			print('.......第%d张......'%x)
			#pic.content
			with open(picstr,'wb') as f:
				f.write(pic.content)
			x+=1
img=image()
flag=True
a=0
b=10
# while flag:
input=raw_input('输入你想要的表情包（Q结束）：')
end=raw_input('需要的表情包数量（1个表情包含60个表情）：')
while flag:
	if input=='Q' or b>(10*int(end)):
		flag=False
		break
	print("第%d个表情包"%(b/10))
	url='http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d&gsm=%d'%(str(input),a,b)
	# url='http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='+str(input)
	page=img.getPage(url)
	img.imgDown(str(input),str(input+'表情'+str(b/10)),page)
	print('下载完成！')
	a,b=b,b+10