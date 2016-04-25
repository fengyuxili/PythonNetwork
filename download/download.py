#encoding:utf-8
#download.py use urllib2 download a file
import urllib2,sys

print "download test with urllib2"
url="http://news.ifeng.com/a/20160424/48564139_0.shtml"
f=urllib2.urlopen(url)
data=f.read()

with open("C:\\test.shtml","wb") as code:
    code.write(data)

print "download %s end" % url
    


