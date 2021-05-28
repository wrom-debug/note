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
* 给指定的key设置存活时间，超时后自动删除 `expire key 秒`
* 查看key存活时间，-2key不存在，-1永久有效 `tty key`
* 给指定的key设置存活时间毫秒单位，超时后自动删除 `pexpire key 毫秒`
* 查看key的存活时间毫秒单位 `pttl key`
* 查找匹配的key，支持通配符 `keys *|字符`
* 移动当前数据库中key到其他数据库上，成功返回1，失败返回0 `move key db`
* 随机获取一个key，但不删除 `randromkey`
* 重命名key，如果源key不存在则报错 `rename key newkey`
* 查看key说存储的数据类型，如果不处在则返回none `type key`
* 在有配置密码进行密码认证 `auth 密码`
* 保存数据 `save`
* 清空数据 `flushall`

## string-字符串

* `set key value [options]`
  * 设置key和value如果key存在，则覆盖
  * `ex` 设置key的存活时间(单位：秒）
  * `px` 设置key的存活时间(单位：毫秒)
  * `nx` 如果设置key不存在则新建，存在不动作返回nil
  * `xx` 只有件存在，才动作
* `get key`
  * 获取key对应的value，只能获取一个key，如果不处在则返回nil
* `mset key value...`
  * 一次设置多个key value关系，已处在则fugai
* `mget key key...`
  * 批量获取key对应的值，如果不处在返回nil
* `getset key value`
  * 给key设置新value，返回旧value，不存在则返回nil
* `strlen key`
  * 返回value的长度
* `append key value`
  * 在key的值后添加新值
* `incr key`
  * key中值加1，value是数字有效
* `dect key`
  * key中值减1，value是数字有效
* `incrby key 值`
  * key中值加指定值，value是数字有效
* `decrby key 值`
  * key中值减指定值，value是数字有效
* `getrange key start end`
  * 切片，左右都包括

## list-序列

* `lpush key value value...`
  * 将一个或多个value插入到key头部
* `lpop key`
  * 移除并返回key的头一个元素
* `lrange key start end`
  * 切片，显示对应范围的元素，左右都包括
* `rpush key value value ...`
  * 将一个或多value插入到的key尾部
* `rpop key`
  * 移除并返回key的尾一个元素
* `rpushx key value value ...`
  * 列表尾部插入，key必须存在
* `lpushx key value value ...`
  * 列表头部插入，key必须存在
* `lindex key 值`
  * 通过索引查找列表中对应的元素
* `linsert key before|after 源value 新value`
  * 将新元素插入到源元素的前面或后面
* `llen key`
  * 获取列表长度
* `lrem key count 元素`
  * 删除列表中的元素
  * count > 0  从头向尾查，删除指定个数的元素
  * count = 0  全部删除
  * count < 0  从尾向头查，删除指定个数的元素
* `lset key count value`
  * 替换索引元素位置的value，索引超范围报错
* `ltrim key start end`
  * 列表切片
  
## hash-字典

* `hset key field value`
  * 给hash增加一组key和value
* `hlen key`
  * 获取hash的长度
* `hget key field`
  * 获取hash中field的值
* `hgettall key`
  * 获取hash key中所有的键值对
* `hmset key field value field value ...`
  * 批量设置hash中的键值对
* `hmget key field field ...`
  * 批量获取hash中的值
* `hsetnx key field value`
  * 给指定的hash增加键值对，如果原来有值则不操作，如果不处在则新增
* `hkeys key`
  * 获取hash中所有的field
* `hvals key`
  * 获取hash中所有的value
* `hexists key field`
  * 判断hash表中fiel是否处在，存在返回1，不存在返回0
* `hincrby key field increment`
  * 给hash表中指定的键值对值加指定整数值，键值对值必须是数字
* `hincrbyfloat key field increment`
  * 给hash表中指定的键值对值加指定浮点数值，键值对必须是数字

## set-无序集合

* `sadd key member ...`
  * 给集合添加值可以添加多个，如果值存在则不动作
* `smember key`
  * 获取集合中所有的成员
* `scard key`
  * 获取集合的成员个数
* `sdiff key key ...`
  * 获取集合的差集
* `sinter key key ...`
  * 获取集合的交集
* `sunion key key ...`
  * 获取集合的并集
* `sismember key member`
  * 判断元素是否存在集合中，存在返回1，不存在返回0
* `smove source destination member`
  * 将member元素从source集合移动到destination集合
* `spop key [count]`
  * 随机删除指定个数的成员并打印出来
* `srandmember key [count]`
  * 随机输出指定个数的元素
  * count > 0
    * count > 集合总数，打印全部成员并无序
    * count < 集合总数，打印count次数随机成员
  * count < 0 打印count绝对值随机成员，会重复
* `srem key member ...`
  * 删除集合中指定元素可以多个

## zset-有序集合

* `zadd key score1 member1 ...`
  * 向有序集合添加一个或多个成员，score是序列号只可以一个一个递增不可以跳着增加
  * 其余与集合一致只是命令开头`s`变成`z`
  
## 订阅与发布

* `subscribe channel...`
  * 订阅一个或多个主题
* `publish channel message`
  * 给指定主题发布内容
* `psubscribe pattern ...`
  * 订阅一个或多个给定模式的频道及a.*（订阅所有a.开头的频道）
* `pubsub channels`
  * 查看当前活跃的主题
* `pubsub numsub channels`
  * 查看当前主题订阅的人数

## redis配置文件

~~~shell

bind 127.0.0.1    # 监听的地址
protected-mode yes # 将redis运行在安全模式下
port 6379 # 端口
tcp-backlog 511
timeout 0
tcp-keepalive 300
daemonize no # 是否以守护进程开启
supervised no
pidfile /var/run/redis_6379.pid
loglevel notice
logfile ""
databases 16
always-show-logo yes
save 900 1  # 在900秒以内有1次更新，就会持久化
save 300 10 
save 60 10000
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb   # 数据的保存文件
dir ./
replica-serve-stale-data yes
replica-read-only yes
repl-diskless-sync no
repl-diskless-sync-delay 5
repl-disable-tcp-nodelay no
replica-priority 100
lazyfree-lazy-eviction no
lazyfree-lazy-expire no
lazyfree-lazy-server-del no
replica-lazy-flush no
appendonly no #开启aof存储
appendfilename "appendonly.aof" #aof文件位置与名称
appendfsync everysec
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
aof-load-truncated yes
aof-use-rdb-preamble yes
lua-time-limit 5000
slowlog-log-slower-than 10000
slowlog-max-len 128
latency-monitor-threshold 0
notify-keyspace-events ""
hash-max-ziplist-entries 512
hash-max-ziplist-value 64
list-max-ziplist-size -2
list-compress-depth 0
set-max-intset-entries 512
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
hll-sparse-max-bytes 3000
stream-node-max-bytes 4096
stream-node-max-entries 100
activerehashing yes
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit replica 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
hz 10
dynamic-hz yes
aof-rewrite-incremental-fsync yes
rdb-save-incremental-fsync yes
requirepass foobared # 给redis设置密码foobared
~~~

## redis主从

~~~shell

只需要在从服务器上进行配置
slaveof ip地址  端口
如果有密码的话
masterauth <password>
命令行设置方式
config set masterauth password
~~~

* 基于异步，平均每秒都会复制主服务器情况
* 一个主可以多个从
* 从也可以有从
* 复制不会柱塞主从服务器

## redis数据持久化

### rdb

* 优点
  * 生成二进制文件
  * 系统会默认的多长时间保存一次
  * 直接手动保存
  * 制作快照
  * 可以用作备份
  * 比较适合做灾难恢复
  * 主进程会fork一个子进程出来，子进程用来复制保存数据
* 缺点
  * 如果说数据需要尽量保存下来，则不适合实用rdb
  * 在数据量庞大的时候，对系统消耗过大

~~~shell

save 900 1  # 在900秒以内有1次更新，就会持久化
save 300 10 
save 60 10000
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb   # 数据的保存文件
dir ./ # 保存目录
~~~

### aof

* 优点
  * 持久化更好
  * aof将所有的操作都追加到一个文件中，redis-check-aof
  * 文件易读
* 缺点
  * 文件会越来越大
  * aof的速度会比rdb慢，aof 使用的是fsync
  * 文件易读

~~~shell

appendonly yes
appendfilename "appendonly.aof"
appendfsync everysec  #储存间隔每秒
~~~

### 使用命令从rdb切换到aof

~~~shell

config set appendonly yes
config set save ""
~~~

## redis事务

~~~shell

multi #开启事务
事务所执行的语句
exec #执行事务，没有回滚机制，不是原子性
~~~

## redis集群

需要6台redis服务器，3主3备，存储的key会依据hash存放到3台主的其中一台

~~~shell

## 6380
bind 127.0.0.1
port 6380
daemonize yes
pidfile 6380.pid
logfile 6380.log
cluster-enabled yes
cluster-config-file node-6380.conf
cluster-node-timeout 10000
## 6381
bind 127.0.0.1
port 6381
daemonize yes
pidfile 6381.pid
logfile 6381.log
cluster-enabled yes
cluster-config-file node-6381.conf
cluster-node-timeout 10000
## 6382
bind 127.0.0.1
port 6382
daemonize yes
pidfile 6382.pid
logfile 6382.log
cluster-enabled yes
cluster-config-file node-6382.conf
cluster-node-timeout 10000
## 6383
bind 127.0.0.1
port 6383
daemonize yes
pidfile 6383.pid
logfile 6383.log
cluster-enabled yes
cluster-config-file node-6383.conf
cluster-node-timeout 10000
## 6384
bind 127.0.0.1
port 6384
daemonize yes
pidfile 6384.pid
logfile 6384.log
cluster-enabled yes
cluster-config-file node-6384.conf
cluster-node-timeout 10000
## 6385
bind 127.0.0.1
port 6385
daemonize yes
pidfile 6385.pid
logfile 6385.log
cluster-enabled yes
cluster-config-file node-6385.conf
cluster-node-timeout 10000
~~~

6台服务器的配置都只是开启cluster，设置超时时间，配置conf文件

### 安装ruby

使用cluster需要安装ruby2.2版本以上

~~~shell

wget https://cache.ruby-lang.org/pub/ruby/2.6/ruby-2.6.4.tar.gz
tar ruby-2.6.4.tar.gz
cd ruby-2.6.4
./configure --prefix=/opt/ruby
make && make install
配置环境变量
PATH=/opt/ruby/bin:$PATH
source 
~~~

#### 安装ruby的依赖库

~~~shell

gem install redis
~~~

### 安装集群

~~~shell

redis-cli --cluster create --cluster-replicas 1(每台服务器有几台备的服务器) 服务器地址1 服务器地址2 服务器地址3 服务器地址4 服务器地址5 服务器地址6

create 创建集群
check 检查集群
info 查看集群
fix 修复集群
~~~

### 链接集群

~~~shell

redis-cli -c 服务器地址
~~~

## python链接

普通链接

~~~python

import redis  #导入redis库
r=redis.StrictRedis(host='192.168.21.128',port=6380,decode_responses=True)  #初始链接
r.set("haoeya","kuaixiake") #设置值
print(r.keys()) #获取所有key

 #语法与redis一致
~~~

集群链接

~~~python

import rediscluster #导入redis-py-cluster库
nodes=[{"host":"192.168.21.128","port":6380},{"host":"192.168.21.128","port":6381},{"host":"192.168.21.128","port":6382},{"host":"192.168.21.128","port":6383},{"host":"192.168.21.128","port":6384},{"host":"192.168.21.138","port":6385}] 

c=rediscluster.RedisCluster(startup_nodes=nodes,decode_responses=True)  #初始链接
print(c.get('name'))
 #语法与redis一致
~~~
