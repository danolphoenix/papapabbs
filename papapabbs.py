#!/usr/bin/python
#coding=utf-8

import sys,os
import re
import random
import time
import urllib,urllib2

__author__ = 'luodan Rodan'
__email__ = 'danolphoenix@163.com'
__github__='https://github.com/danolphoenix'

#Hi all, this is an easy reptilian (Sorry ,I really dont know how to call it)
#to help you get the pictures in the comment of bbs.uestc.edu.cn.
#the picture in the comment will be named after its author's name.
#if the name has existed, then the picture will be named after its author's name + a random number with range(1,1000)
#hope you have fun

# the range of the postpage, which depends on the total count of the postpage.
for page in range(1,10):
    print page
    postUrl = 'THE ADDRESS OF THE POST' # such as 'http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=XXXXXXX' ,REMEBER THE QUOTES
    url = postUrl +'&extra=&page=' + str(page)

	###############pretend browser################
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    cookie = 'THE COOKIES OF THE BROWSER' # you can get it in chrome with CTRL+SHIFT+I,REMEBER THE QUOTES
    headers = {'User-Agent' : user_agent,
            'cookie' : cookie}

	#############get the page content#######
    try :
        request = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
		
		###########get authors and the comment content###########
        reg = r'<div id="post_.*?class="xw1">(.*?)</a>.*?<td class="plc"(.*?)<a class="cmmnt"'
        pattern = re.compile(reg, re.S)
        items = re.findall(pattern, content)
        for item in items:
            #item[0] is the author,and item[1]is the comment content
			############get the imgurl in the comment content########
            content_reg = r'zoomfile.*?(data/attachment/forum.*?(?:jpg|png|bmp))'
            content_pattern = re.compile(content_reg, re.S)
            zoom_img_urls = re.findall(content_pattern, item[1])
			
            if  (len(zoom_img_urls)!=0) :
                print item[0]
                #import pdb;pdb.set_trace()
                for zoom_img_url in zoom_img_urls:
                    ###########get the extension name of the picture#################
                    extension_re = r'.*\.(.*$)'
                    extension_pattern = re.compile(extension_re)
                    extension_name = re.findall(extension_pattern, zoom_img_url)

                    imgurl = r'http://bbs.uestc.edu.cn/' + zoom_img_url
                    print imgurl

                    if not os.path.exists(os.getcwd() + "\\" + item[0] + '.'+ extension_name[0]):
                        urllib.urlretrieve(imgurl, item[0].encode(sys.getfilesystemencoding())+'.'+str(extension_name[0]) )
                    else:
                        urllib.urlretrieve(imgurl, item[0].encode(sys.getfilesystemencoding())+'('+str(random.randrange(0,1001))+')'+'.'+ str(extension_name[0]) )                        

    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
