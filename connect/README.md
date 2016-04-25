# 网络编程 connect
* socket模块 调用模块内成员使用socket.成员
* 根据通信类型AF_INET(IPV4) SOCK_STREAM IO流(TCP) SOCK_DGRAM(UDP数据报)创建socket
* getservbyname 根据服务和传输协议类型查找端口号
* connect 根据服务端地址和端口连接

example:
```python
import socket
host = www.baidu.com
try:
    port = socket.getservbyname('http','tcp')
except socket.error,e:
    print "Count not find your port:%s" % e
    sys.exit(1)
		
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((host,port)) # use tupple
except socket.gaierror, e:
    print "Address-relate error connecting to server: %s" %e
    sys.exit(1)
except socket.error, e:
    print "Connection error:%s" %e
    sys.exit(1)
s.close()
```
