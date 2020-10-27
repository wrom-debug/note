# django {ignore}

[toc]

---

## web框架本质

使用socket简单实现web框架功能

~~~python

import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8001))
sk.listen()
conn,addr = sk.accept()
from_b_msg = conn.recv(1024)
str_msg = from_b_msg.decode('utf-8')
conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
conn.send(b'hello')
~~~

http请求格式

()[]
