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
#to help you get reply of someone in a post of bbs.uestc.edu.cn.
#the picture in the comment will be named after its author's name.
#if the name has existed, then the picture will be named after its author's name + a random number with range(1,1000)
#hope you have fun

file_object = open('reply.txt', 'a+')


# the range of the postpage, which depends on the total count of the postpage.
for page in range(300,377):
    print page
    postUrl = '' # such as 'http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=XXXXXXX' ,REMEBER THE QUOTES
    url = postUrl +'&extra=&page=' + str(page)

	###############pretend browser################
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    cookie = ''
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
        if items[0] != "user":
            continue
        for item in items:
            #item[0] is the author,and item[1]is the comment content
			############get the imgurl in the comment content########
            content_reg = r'postmessage.*?>(.*?)</td>'
            content_pattern = re.compile(content_reg, re.S)
            replycontent = re.findall(content_pattern, item[1])
			
             
            print item[0]+":"
            #import pdb;pdb.set_trace()
             
            print replycontent
            file_object.write(item[0].encode(sys.getfilesystemencoding()))
            file_object.write('\n')
            file_object.write(replycontent[0].encode(sys.getfilesystemencoding()))
            file_object.write('\n')
            file_object.write('\n')
                   
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

file_object.close()