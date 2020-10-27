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

![http请求格式](img/2.jpg "http请求格式")

示例：

~~~http

GET / HTTP/1.1
Host: 127.0.0.1:8001
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6
Cookie: csrftoken=wbpwiMbku4CIpXWMAb8KiTudh2gPKHC9eaMjnriN4fFSP6dcgRuXwS27GH3eYKtp
~~~

http响应格式

!["http相应格式"](img/3.jpg "http相应格式")

示例：

~~~http


~~~
