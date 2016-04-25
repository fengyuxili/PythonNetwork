#encoding:utf-8
#basic connection example

import socket,sys,time

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

#print "argv[1]=",sys.argv[1]
#print "argv[2]=",sys.argv[2]
#print "argv[3]=",sys.argv[3]

print "Creating socket"
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
    print "Strange error creating socket:%s" %e
    sys.exit(1)


try:
    port = int(textport)
except ValueError:
    # if didn't work,look up instead
    try:
        port = socket.getservbyname('http','tcp')
    except socket.error,e:
        print "Count not find your port:%s" % e
        sys.exit(1)
try:
    s.connect((host,port)) # use tupple
except socket.gaierror, e:
    print "Address-relate error connecting to server: %s" %e
    sys.exit(1)
except socket.error, e:
    print "Connection error:%s" %e
    sys.exit(1)

print "sleeping" #sleep and wait for connect to  server
time.sleep(1)
print "continue"

"""
#使用了文件类对象
#makefile创建一个与该套接字相关连的文件#
fd = s.makefile('rw',0)

try:
    fd.write("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, e:
    print "Error sending data: %s" % e
    sys.exit(1)
try:
    fd.flush()
except socket.error, e:
    print "Errot sending data (detected by flush):%s" % e
    sys.exit(1)
"""
try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, e:
    print "Error sending data: %s" % e
    sys.exit(1)

#0代表禁止下次的数据读取；1代表禁止下次的数据写入；2代表禁止下次的数据读取和写入
#shutdown()来判断数据是否发送成功，只有缓存中的数据发送成功，shutdown 才会返回
#shutdown应该在最后一次发送数据时调用，因为调用shutdown(1)后就是单工了
#要想确保数据被发送也可以使用timeout
try:
    s.shutdown(1) 
except socket.error, e:
    print "Errot sending data (detected by shutdown):%s" % e
    sys.exit(1)
    

print "Connect from",s.getsockname() # local host and port
print "Connect to",s.getpeername()   #remote ip address and port

while 1:
    try:
        buf =s.recv(2048)
    except socket.error, e:
        print "Error receiving data:%s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)
