import struct
import socket as _socket
from socket import *

_GLOBAL_DEFAULT_TIMEOUT = _socket._GLOBAL_DEFAULT_TIMEOUT
proxy_address = ()

class socket(_socket.socket):
    def __init__(self, *args):
        super().__init__(*args)

    def connect(self, address):
        super().connect(proxy_address) # socks5 proxy

        ####################### socks5 proxy connection #######################
        # greet the socks server
        msg = struct.pack("!BB", 0x05, 1) # auth_methods_available = 1
        msg += struct.pack("!B", 0x00) # auth_methods = [0x00]
        self.send(msg)
        resp = self.recv(2)
        (version, auth_method) = struct.unpack("!BB", resp)

        host, port = address

        # set connection to tcp/ip stream, ipv4
        ipb = list(map(int, _socket.gethostbyname(host).split("."))) # hostname -> ip
        msg = struct.pack("!B B B B BBBB H",0x05,0x01,0x00,0x01,ipb[0],ipb[1],ipb[2],ipb[3],port)
        self.send(msg)
        resp = self.recv(10)
        (version, status) = struct.unpack("!B B 8x", resp)

        # check status
        if status != 0:
            self.close()
            raise Exception("socks connection failed, error: " + str(status))

def create_connection(*args):
    s = socket()
    s.connect(args[0])
    return s
