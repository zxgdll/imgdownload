#!/usr/bin/env python
#coding=utf-8
import urllib2
import re
import requests
import threading
import os
class image:
	def __init__(self):
		self.enable=False
		self.a=0
		self.b=10
		self.word=''
		self.Imgs=[]
	def getPage(self,a,b):
		try:
			url='http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d&gsm=%d'%(str(self.word),a,b)
			request=urllib2.Request(url)
			response=urllib2.urlopen(request)
			page=response.read().decode('utf-8')
			return page
		except urllib2.URLError as e:
			if hasattr(e,'reason'):
				print(e.reason)
			return None
	def getImg(self,a,b):
		page=self.getPage(a,b)
		pattern=u'\"objURL\":\"(.*?)\"'
		items=re.findall(pattern,page,re.S)
		Img=[]
		for item in items:
			Img.append(item)
		return Img
	def Imgdown(self,newpath,num,Img):
		x=0
		for image in Img:
			try:
				pic=requests.get(image,timeout=150)
			except requests.exceptions.ConnectionError:
				print('[ERROR]:down failed!')
				continue
			picpath=newpath+'/'+'表情包'+str(num)+r'_'+str(x)+'.jpg'
			print('.......表情包%d第%d张......'%(num,x))
			with open(picpath,'wb') as f:
				f.write(pic.content)
			x+=1
	def loadImg(self):
		if self.enable:
			if len(self.Imgs)<2:
				pageImg=self.getImg(self.a,self.b)
				if pageImg:
					self.Imgs.append(pageImg)
					self.a,self.b=self.b,self.b+10

	def start(self):
		input=raw_input('输入需要的表情包名称(Q结束)：')
		end=raw_input('需要的表情包数量(每个表情包含有60个)：')
		self.word=input
		self.enable=True
		self.loadImg()
		newpath=os.path.join('pics/',input)
		if not os.path.exists(newpath):
			os.mkdir(newpath)
		num=1
		while self.enable:
			if input=='Q' or (num>int(end)):
				self.enable=False
				break
			if len(self.Imgs)>0:
				print(u'第%s个表情包'%str(num))
				pageImg=self.Imgs[0]
				del self.Imgs[0]
				self.Imgdown(newpath,num,pageImg)
				print('第%d个表情包下载完成！'%num)
				num+=1
img=image()
img.start()


