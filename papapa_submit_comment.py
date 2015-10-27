#-*-coding:utf-8-*-  
#lilybbs.py  
#Author:Sky_Money  
#Python实现自动登录BBS并发帖  
  
import urllib,urllib2  
 
request_url='http://bbs.uestc.edu.cn/forum.php?mod=post&action=reply&fid=25&tid=1566411&extra=&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'

#下面是发帖验证   
sendCookie= 

#发送的Headers，必须要有Cookie  
sendheaders = {  
 	'Referer':'http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=1566411&extra=&page=25',
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
 	'Content-Type':'application/x-www-form-urlencoded'
}  
  
sendheaders['Cookie']=sendCookie  
 
#发帖的data主体  
body=urllib.urlencode({#'formhash':'433c34ea',
'subject':'回帖标题',
'formhash':'433c34ea',
'message':'回帖内容'}
)

returnedReq=urllib2.Request(  
    url=request_url,  
    data=body,  
    headers=sendheaders)  
returnedResult=urllib2.urlopen(returnedReq).read()
import pdb
pdb.set_trace()
import sys
print returnedResult