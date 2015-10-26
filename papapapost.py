#-*-coding:utf-8-*-  

import urllib,urllib2  

request_url=' '
  
#下面是发帖验证  
  
  
sendCookie= 
#发送的Headers，必须要有Cookie  
sendheaders = {  
	'Host':' ',
	'Origin':' ',
	'Referer':'http://bbs.uestc.edu.cn/forum.php?mod=post&action=newthread&fid=25',
	'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip,deflate,sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Length':'363',
	'Content-Type':'application/x-www-form-urlencoded'
}  
  
sendheaders['Cookie']=sendCookie  
  
#发帖的data主体  
body=urllib.urlencode({'formhash':'433c34ea',
'wysiwyg':1,
'typeid':315,
'subject':'test试试2',
'message':'keep silence',
'price':'',
'tags':'',
'cronpublishdate':'',
'allownoticeauthor':1,
'addfeed':1,
'usesig':1,
'uploadalbum':3909,
'newalbum':'请输入相册名称'}
)
import pdb
pdb.set_trace()
returnedReq=urllib2.Request(  
    url=request_url,  
    data=body,  
    headers=sendheaders)  
returnedResult=urllib2.urlopen(returnedReq).read()
 
print returnedResult  
