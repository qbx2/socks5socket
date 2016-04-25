# socks5socket #
### example ###
```
import socks5socket
socks5socket.proxy_address=('localhost',9050)
import sys
sys.modules['socket']=socks5socket
import http.client
c=http.client.HTTPConnection('ipip.kr')
c.request('GET','/')
c.getresponse().read()
```
