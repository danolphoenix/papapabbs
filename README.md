# papapabbs.py
a python crawler to retrieve the picture in the qshpan bbs
Hi all, this is an easy crawler (Sorry ,I really dont know how to call it) 
to help you get the pictures in the comment of bbs.uestc.edu.cn.

It based on urllib,urllib2.

I heard that requst lib is better,maybe I will try it when free.

If you are not the student of uestc, skip it.you can't login in it :P

The picture in the comment will be named after its author's name.
If the name has existed, then the picture will be named after 
its author's name + a random number with range(1,1000)

you need to add the POSTPAGENUM， POST ADDRESS and COOKIES in the code. then use

$ python papapabbs.py

it will download pictures and store them in the current path.

Hope you have fun.

# pacohng.py
the other file pacohng.py is to help you get all the picture in the specific page such as www.163.com.
