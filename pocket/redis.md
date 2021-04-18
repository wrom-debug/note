# redis

[toc]

## 介绍

redis是内存型、非关系型、键值型数据库

## 安装

* 使用yum安装，但是需要先配置epel源

~~~shell

yum install redis
~~~

* 编译安装

~~~shell

wget http://download.redis.io/releases/redis-5.0.5.tar.gz
tar xf redis-5.0.5.tar.gz
cd redis-5.0.5/
make
~~~

### 安装后可执行文件

~~~shell

wget http://download.redis.io/releases/redis-5.0.5.tar.gz
tar xf redis-5.0.5.tar.gz
cd redis-5.0.5/
make
~~~

## 启动redis

~~~shell

redis-server    #默认端口6379，默认占用终端
也可以在后面跟上conf配置文件
~~~

## 性能测试

~~~shell

redis-benchmark -q  #默认是10w次链接50个客户端同是链接
-c 指定同时链接数量
-n 总链接次数
~~~

## 连接

~~~shell

redis-cli -h ip地址 -p 端口 -s sock文件 -a 密码 -n 进入的数据库编号 
~~~

## 数据类型

* string 字符串
* hash 哈希（字典）
* list 列表
* set 集合
* zset 权重集合

## 命令

redis的命令是不区分大小写的

### 基础

* 测试是否链接数据库，连通返回pong `ping`  
* 查看系统信息，也可以在后面跟标签只查看标签信 `info [标签]`
* 打印 `echo 所需打印的内容`
* 断开连接 `quit`
* 切换到对应数据库 `select 数据库编号`
* 删除key `del 要删除的key`
* 判断key是否存在，处在返回1，不存在返回0 `exists key`
* 