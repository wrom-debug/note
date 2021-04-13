# nginx

[toc]

## 安装

~~~shell

wget http://nginx.org/download/nginx-1.16.1.tar.gz
tar xf nginx-1.16.1.tar.gz 
cd nginx-1.16.1
yum install gcc zlib2-devel pcre-devel openssl-devel
 ./configure --prefix=/opt/nginx --with-http_ssl_module --with-http_stub_status_module
 make && make install

yum install nginx
~~~

## 目录结构

* conf 配置文件
* html 存放静态文件
* logs 日志目录
* sbin 二进制文件

## 配置文件

nginx.conf

~~~shell

user  nginx;    #起进程的用户
worker_processes  1;    #工作进程数量

error_log  /var/log/nginx/error.log warn;   #错误日志
pid        /var/run/nginx.pid;  #pid参数


events {
    worker_connections  1024;   #最大连接数
}


http {
    include       /etc/nginx/mime.types;    #导入
    default_type  application/octet-stream; #请求格式

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"'; #定义log格式

    access_log  /var/log/nginx/access.log  main;    #连接日志

    sendfile        on; 
    #tcp_nopush     on;

    keepalive_timeout  65;  #长连接

    #gzip  on;  #是否压缩

    include /etc/nginx/conf.d/*.conf;   #导入conf文件夹
}

~~~

/etc/nginx/conf.d/default.conf

~~~shell

upstream djang {
        server 192.168.0.108:80;    #定义集群
        server 192.168.0.110:80;
}

server {
    listen       80;    #监视端口
    server_name  localhost; #定义域名

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;

    location / {    #连接路由
        root   /data/dj;    #定义根路径目录
        index  index.html index.htm;   #根路径初始网站
 }

    #error_page  404              /404.html;    #404报错显示网站

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;    #50开头报错显示网页
    location = /50x.html {  
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
~~~

### 日志

~~~shell

remote_addr 访问的ip地址
remote_user 访问用户
time_local 本地时间
requset 包括请求方式 请求地址 请求版本
status 状态码
body_bytes_sent 响应发送的大小
http_user_agent 用户请求头
http_x_forwarded_for http拓展头部
~~~

### root和alias区别

~~~shell

在server结构内

location /路径{
    root /data/dj;  
    }
location后面内容 root后面路径下必须有相同路径的相同文件

lication /路径{
    alias /data/dj;    
}
locarion后面内容 alias后面路径不许要有相关路径只需要有对应文件就可以了
~~~

### 域名

~~~shell

在server结构内

server_name www.worm.com #将对应域名的请求使用本server中的location来进行路由分发，由于没有向运行商dns服务申请需要在客户端电脑中改写host修改dns解析规则。
~~~

### 多域名

是使用一台设备运行多个域名的方式

~~~shell

server{ #域名1服务器
    listen 80;
    server_name www.taobao.com taobao.com;
    location / {
        root /data/taobao;
        index index.html;
        }
}

server{ #域名2服务器
    listen 80;
    server_name www.jd.com jd.com;
    location / {
        root /data/jd;
        index index.html;
        }
}
~~~

工作流程

~~~mermaid

graph LR
    A[客户端发起请求] -->B[本机dns解析域名ip]
    B --> C[服务器收到请求]
    C --> D{nginx判断域名将请求分配给对应的server}
    D --> |请求为server1的域名| E[sercer1进请求后面的路径通过location进行路由转发]
    D --> |请求为server2的域名| F[sercer2进请求后面的路径通过location进行路由转发]
~~~

### 默认server

在只输入ip时使用设置了默认seerver的server来相应请求

~~~shell

listen 80 default_server；
~~~

### 禁止访问

指定相关ip禁止|允许访问

~~~shell

可以写在server中或者写在location中

deny 192.168.0.1；  #禁止这个ip访问
allow 192.168.0.2； #允许这个ip访问
deny 192.168.0.0/24;    #禁止这个网段访问(小范围写在大范围前)
~~~

### 反向代理

工作流

~~~mermaid

graph LR
    A[客户端] --> B{对外服务器 公网ip}
    B --> |反向代理转发| C[内部服务器1 内网ip]
    B --> |反向代理转发| D[内部服务器2 内网ip]
~~~

* 由于该工作流所有外部客户端不可以直接访问到内部服务器，起到了保护网站的作用
* 可以实现缓存静态文件
* 实现负载均衡，访问量可以为两台服务器之和
* 实现该方式最少需要3个server，一台做访问ip，两个做被访问

~~~shell

范围ipserver这样配置
upstream django {
server 192.168.21.128:81;
server 192.168.21.131:81;
}   #定义
server {
listen 80 default_server;
listen [::]:80 default_server;
server_name _;
# Load configuration files for the default server block.
include /etc/nginx/default.d/*.conf;
location / {
proxy_pass http://django;
}
其他被转发server正常设置，但是要保障域名或着端口要不一样
~~~

这样设置会一次访问server1一次访问server2（均衡）

#### 权重

~~~shell

upstream django {
    server 192.168.21.128:81 weight=3;
    server 192.168.21.131:81
}   #权重越大访问次数越多
~~~

#### ip_hash

对每个请求做hash运算，这样每个ip访问都会固定到后端固定的机器上

~~~shell
upstream django {
    ip_hash;
    server 192.168.21.128:81
    server 192.168.21.131:81
}
~~~

#### backup

只有前面都访问不到时，才会请求backup，只要一个通就不会走backup

~~~shell

upstream django {
    server 192.168.21.128:81;
    server 192.168.21.131:81;
    server 192.168.21.131:82 backup;
}
~~~

#### fair

响应时间短的优先

~~~shell

upstream backserver { 
    server server1; 
    server server2; 
    fair; 
} 
~~~

#### url_hash

相同rul都会指向同一台server，减少缓存时间

~~~shell

upstream backserver { 
    server squid1:3128; 
    server squid2:3128; 
    hash $request_uri; 
    #hash_method crc32; 
} 
~~~

#### least_conn

~~~shell
upstream dynamic_zuoyu {
        least_conn;    #把请求转发给连接数较少的后端服务器
        server localhost:8080   weight=2;  #tomcat 7.0
        server localhost:8081;  #tomcat 8.0
        server localhost:8082 backup;  #tomcat 8.5
        server localhost:8083   max_fails=3 fail_timeout=20s;  #tomcat 9.0
    }
~~~

### location

#### location匹配规则

~~~shell

location = / {
    精确匹配/ ,后面不能带其他的东西
    [ configuration A ]
}

location / {
    所有的以/开头的地址
    [ configuration B ]
}

location /documents/ {
    匹配/documents/
    [ configuration C ]
}

location ^~ /images/ {
    # 匹配以/images/开头。
    ~严格大小写
    [ configuration D ]
}

location ~* \.(gif|jpg|jpeg)$ {
    以(gif|jpg|jpeg)结尾的文件
    ~* 不区分大小写
    [ configuration E ]
}
优先级
= > 完整路径 > ^~ > /
~~~

#### location分离

实现动静分离

~~~sehll

server  {

        listen 80 ;
        server_name www.taobao.com taobao.com;
        location / {
        proxy_pass http://192.168.21.131:82;
        }
        location ~*\.(jpg|gif|png)$ {
        root /data/img;
        }
~~~
