# socks5socket #
### example ###
```
import socks5socket
socks5socket.proxy_address=('localhost',9050)
import http.client
# import sys
# sys.modules['socket']=socks5socket
# or
http.client.socket = socks5socket
c=http.client.HTTPConnection('ipip.kr')
c.request('GET','/')
c.getresponse().read()
```
