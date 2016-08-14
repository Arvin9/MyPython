# -*- coding:utf-8 -*-

import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print ip

ipList = socket.gethostbyname_ex(hostname)
print ipList[2][1]
