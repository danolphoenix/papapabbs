#!/bin/python
#-*-coding:utf-8-*-  
 
#Python实现论坛发帖和回复
  
import urllib,urllib2  

#发帖地址,fid表示板块号码，25为水区
request_url='http://bbs.uestc.edu.cn/forum.php?mod=post&action=newthread&fid=25&extra=&topicsubmit=yes'

#cookie  
sendCookie= 

#发送的Headers，必须要有Cookie  
sendheaders = {  
	'Referer':'http://bbs.uestc.edu.cn/forum.php?mod=post&action=newthread&fid=25',
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	'Content-Type':'application/x-www-form-urlencoded'
}  
  
sendheaders['Cookie']=sendCookie  
 
#发帖的data主体  
body=urllib.urlencode({
'formhash':'433c34ea' #必需字段
'subject':'我想试试这个字段有啥用呢'#发帖标题
'message':'程序员的工资将会下降到正常状态'#帖子内容
)

returnedReq=urllib2.Request(  
    url=request_url,  
    data=body,  
    headers=sendheaders)
returnedResult=urllib2.urlopen(returnedReq).read()
import pdb
pdb.set_trace()
print returnedResult