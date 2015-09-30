import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
#    html = 'src="http://img3.cache.netease.com/img09/space.gif" data-original-src="http://img5.cache.netease.com/cnews/2015/8/20/20150820085747706ca.jpg1234"'
    return html

def getImg(html):
    reg = r'http?://\w+(?:\.[^\.]+)+(?:/.+)*/.+\.jpg'
    reg = r'src=.{1}http?://.*?\.jpg?'
    reg = r'\"http.*?jpg'
    reg = r'http\://[^\s]+jpg|http\://[^\s]+png'
    reg = r'http\://[^\s]+(?:jpg|png|gif)'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist


html = getHtml("http://www.163.com")
for link in getImg(html):
    print link

