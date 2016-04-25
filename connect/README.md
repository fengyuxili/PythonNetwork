# ������ connect
* socketģ�� ����ģ���ڳ�Աʹ��socket.��Ա
* ����ͨ������AF_INET(IPV4) SOCK_STREAM IO��(TCP) SOCK_DGRAM(UDP���ݱ�)����socket
* getservbyname ���ݷ���ʹ���Э�����Ͳ��Ҷ˿ں�
* connect ���ݷ���˵�ַ�Ͷ˿�����

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
