# download by 3 ways

* one urllib

```python
import urllib 
print "downloading with urllib" 
url = 'http://www.pythontab.com/test/demo.zip'  
print "downloading with urllib"
urllib.urlretrieve(url, "demo.zip")
```
* two urllib2

```python
import urllib2
print "downloading with urllib2"
url = 'http://www.pythontab.com/test/demo.zip' 
f = urllib2.urlopen(url) 
data = f.read() 
with open("demo2.zip", "wb") as code:     
    code.write(data)
```
* three requests

```python
import requests 
print "downloading with requests"
url = 'http://www.pythontab.com/test/demo.zip' 
r = requests.get(url) 
with open("demo3.zip", "wb") as code:
     code.write(r.content)	
```