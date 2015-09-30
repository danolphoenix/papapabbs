#!/usr/bin/python
#coding=utf-8

import sys,os

import re
import time
import urllib,urllib2

# reload(sys)
# sys.setdefaultencoding('utf-8')
# try:
    # import apport_python_hook
# except ImportError:
    # pass
# else:
    # apport_python_hook.install()


def getHtml(url):
	#page = urllib.urlopen(url)
	#html = page.read()
 	html = '<img id="aimg_1694151" aid="1694151" src="static/image/common/none.gif" zoomfile="data/attachment/forum/201505/30/213528etghay0h2uhyb2na.jpg" file="data/attachment/forum/201505/30/213528etghay0h2uhyb2na.jpg" class="zoom"'
	return html

def getImg(html):
    import pdb
    pdb.set_trace()
    reg = r'class="xw1">(.*?)</a>.*?(data/attachment/forum.*?jpg)'
    reg = r'<div.*?class="xw1">(.*?)</a>.*?zoomfile.*?(data/attachment/forum.*?jpg)'
    imgre = re.compile(reg)
    author_img_list = re.findall(imgre, html)
    print author_img_list
    for author_img in author_img_list:
        author = author_img[0]
        imgurl = r'http://bbs.uestc.edu.cn/' + author_img[1]
        print imgurl
        urllib.urlretrieve(imgurl, '%s.jpg' % author)

	# max = 0
	# for i,imgurl in enumerate(imglist):
		# print imgurl
		# urllib.urlretrieve(imgurl, '%s.jpg' %i)
		# max+=1
		# if max==20:
			# time.sleep(0.1)
			# max = 0


for page in range(1,9):
    print page
    url = 'http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=1522728&extra=&page=' + str(page)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    cookie = 
    headers = {'User-Agent' : user_agent,
            'cookie' : cookie}
    try :
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        # getImg(response.read().decode('utf-8'))
        content = response.read().decode('utf-8')
        reg = r'class="xw1">(.*?)</a>.*?zoomfile.*?(data/attachment/forum.*?(?:jpg|png)).*?<div'

        reg = r'<div id="post_.*?class="xw1">(.*?)</a>.*?<td class="plc"(.*?)<a class="cmmnt"'
		
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, content)
       
        
        for item in items:
            # print item[0].encode('utf-8'),item[1]
            #author = item[0].encode('utf-8')
            print item
            #import pdb
            #pdb.set_trace()
			
			
            urlreg = r'zoomfile.*?(data/attachment/forum.*?(?:jpg|png))'
            urlpattern = re.compile(urlreg, re.S)
            urlresult = re.findall(urlpattern, item[1])	
            if  (len(urlresult)!=0) :			
                imgurl = r'http://bbs.uestc.edu.cn/' + urlresult[0]
                print item[0]
                print imgurl
				
				
                #import pdb
                #pdb.set_trace()
                urllib.urlretrieve(imgurl, item[0].encode(sys.getfilesystemencoding())+'.jpg' )
                #import pdb
                #pdb.set_trace()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
