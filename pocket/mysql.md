# SQL

[toc]

## 安装myqsl

ubuntu

~~~SHELL
sudo apt-get install mysql-server
sudo apt-get install mysql-client
~~~

可以在/etc/mysql/debian.cnf中查看默认账户密码

centos

下载

~~~shell

wget http://mirrors.sohu.com/mysql/MySQL-5.7/mysql-5.7.27-1.el7.x86_64.rpm-bundle.tar
~~~

解压

~~~shell
tar xf MySQL-5.6.44-1.el7.x86_64.rpm-bundle.tar
~~~

安装

~~~shell
yum install -y *.rpm
~~~

默认安装位置：/var/lib/mysql

报错信息：

~~~sehll
2019-08-30T11:18:22.976635Z 0 [Warning] Can't create test file /mydata/mysql/localhost.lower-test
2019-08-30T11:18:22.976687Z 0 [Note] /usr/sbin/mysqld (mysqld 5.7.27) starting as process 2788 ...
2019-08-30T11:18:22.980289Z 0 [Warning] Can't create test file /mydata/mysql/localhost.lower-test
2019-08-30T11:18:22.980338Z 0 [Warning] Can't create test file /mydata/mysql/localhost.lower-test

原因：selinux开启
解决办法：setenforce 0
~~~

重置密码

~~~shell
默认密码：
grep 'pass' /var/log/mysqld.log
mysql_secure_installation
输入root密码
是否要修改密码
是否要修改root密码（大小写、数字、特殊字符）
是否要删除匿名用户
是否禁止root远程登录
是否要删除test数据库
是否要刷新表的权限
~~~

密码校验规则

~~~shell
设置密码的校验规则
mysql> set global validate_password_policy=0;
0 校验级别最低，只校验密码的长度，长度可以设定
1 必须包括大写字母、小写字母、数字、特殊字符
2 必须满足上面两条，并追加，对于密码中任意连续的4个（或者4个以上） 字符不能是字典中的单词
mysql> set global validate_password_length=3; 修改密码的最短长度
~~~

### myql的一般操作

~~~SHELL
service mysql start     #启动
service mysql stop      #停止
service mysql restart       #重启
~~~

### 登录

~~~SHELL
mysql -h地址 -u账户 -p密码
~~~

### 设置客户端地址

修改`/etc/mysql/mysql.conf.d/mysqld.cnf`注释如下内容

~~~shell
bind-addrs =127.0.0.1
~~~

### 修改默认帐号和密码

~~~SQL
mysql> update mysql.user set authentication_string=password('new passwd') where user='root' and Host ='localhost';

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
~~~

## 用户操作

### 添加一个用户

~~~SQL
create user "用户名"@"地址"   identified by "密码"    #地址栏可以使用%来代表任意网段
~~~

### 修改密码

~~~SQL
set password=password("设置的密码");
~~~

### 设置权限

~~~SQL
grant 权限类型[all全部      select 查       insert 写入 ] on 数据库.表 to 用户名@地址;
~~~

可以再设置权限时直接补上密码部分，来实现创建用户

### 刷新用户配置

~~~SQL
flush privileges;
~~~

### 查看用户

~~~SQL
select user from mysql.user
~~~

## 数据库操作

### 查看数据库

~~~SQL
show databases;
~~~

### 创建数据库

创建名为wormdb的数据库，编码格式为utf-8

~~~SQL
create database wormdb charset=utf8;
~~~

### 查看数据库u编码格式

查看wormdb的编码格式

~~~SQL
show create database wormdb;
~~~

### 查看当前所在库

~~~SQL
select database();
~~~

### 切换库

切换至wormdb库

~~~SQL
use wormdb;
~~~

### 删除库

~~~SQL
drop database wormdb;
~~~

## 表操作

### 添加表

~~~SQL
create table maoyan_1 (列内容 )type=引擎名称;
~~~

Innodb：（数据和索引存一起）数据索引/表结构（事务、行级锁、表级锁、外键）
Myisam：（数据和索引分开存储）数据/索引/表结构（支持表级锁）
Menory：（数据在内存上）表结构

### 查看数据库中的表

~~~SQL
show tables;
~~~

### 查看表的列结构

~~~SQL
desc 表名;
~~~

### 查看表构成

可以查看编码格式，数据库引擎，列字段

~~~SQL
show create table 表名
~~~

### 删除表

~~~SQL
drop table 表名;
~~~

## 记录操作

### 插入

~~~SQL
insert into 表名(字段1，......)values(值1,....);
insert into 表名 values (值1),(值2);
~~~

### 查询

~~~SQL
select 列表名 from 表名 [where 条件];
select * from 表名 [where 条件];
~~~

### 更新

~~~SQL
update 表名 set 字段=值;
~~~

### 删除

~~~SQL
delete from 表名 where 条件;
truncate table 表名;    #清空表，和自增偏移量
~~~

## 字段操作

### 添加

~~~SQL
alter table 表名 add 字段 类型;     #在最后添加
alter  table 表名 add 字段 类型 first;      #在开头添加
alter  table 表名 add 字段 类型 after 字段;     #在字段后添加
~~~

### 删除字段

~~~SQL
alter table 表名 drop 字段名;
~~~

### 修改字段类型

~~~SQL
alter table 表名 modify 字段名 新类型
~~~

### 修改字段

~~~SQL
alter table 表名 change 旧字段  新字段 类型
~~~

### 重命名表

~~~SQL
alter table 旧表名 rename 新表名
~~~

## 高级搜索

### 模糊匹配

~~~SQL
select 字段 form 表名 where 字段 like 条件
select 字段 form 表名 where 字段 regexp 条件（正则表达式）
~~~

模糊查询用%代替任何字符

### 排序

~~~SQL
selcet 字段 from 表名 where 条件 order by 字段 [ASC/DESC]
~~~

ASC：升序
DESC：降序

### 字段重命名

~~~SQL
select 字段 as 新名称 from 表;
select 字段 新名称 from 表;
~~~

### 字段内容去重

~~~SQL
select distinct 字段 from 表;   #如果多字段就联合去重 类似联合唯一
~~~

### 拼接函数

~~~SQL
select concat(字段1，“：”，字段2) from 表;    #可以将字段1和2的内容进行类似字符串拼接
select concat(“：”，字段1，字段2) from 表;  
~~~

### 条件判断

~~~SQL
select (case when 条件 then 执行 else 执行2 end) from 表;
~~~

### 范围

~~~SQL
between 数值1 and 数值2 #再数值1和数值2之间
in (数值1,数值2) 只匹配数值1和数值2
~~~

### 分组

~~~SQL
select  聚合函数（字段）from 表 group by 字段 #将记录按照字段的不同值分组，可以配合聚合函数统计每组的数量，最大，最小，平均等值
~~~

count（）求个数
max（）最大值
min（）最小值
sum（）求和
avg（）求平均

### 显示分组内的所有内容

~~~SQL
select 之段1  group_concat(字段2) ftom 表 group by 字段1 ;      #将记录按字段1分组，并显示每组中字段2的记录
~~~

### 过滤

~~~SQL
select 之段1  group_concat(字段2) ftom 表 group by 字段1  having max(字段3)>100;  
~~~

having 与where一样，不过是对组进行过滤，后面一般更聚合的判断

### 分页

~~~SQL
select 字段 from  表名 where 条件 limit  开始记录，数量
limit n offset m 是一样的
~~~

显示多少条

### 联合查询

~~~SQ;
select 字段 from 表名 where 条件 union [all] select 字段 from 表名 where 条件
~~~

all，将重复的记录重复显示

两次查询的显示字段要一样

### 多表查询

~~~SQL
select 表名1.字段1 ，表名2.字段2 from 表名1 ，表明2where 条件
~~~

### 内连接（一般使用内连接方式，不使用多表查询）

~~~SQL
select * from 表1 inner join 表2 on 条件/（表1.字段1=表2.字段2）    #显示表1与表2中字段1和2都有的记录
~~~

同理还有左内连接，又内连接，全内连接（显示左表全部内容+内连接）、（显示右表全部内容+内连接）

~~~SQL
select * from 表1 left join 表2 on 条件
select * from 表1 right join 表2 on 条件
select * from 表1 full join 表2 on 条件(mysql没有这个)
~~~

### 子查询

可以将一个slect 查询的结果用括号包起来表示结果，用在另一个select查询中的条件中，括号中的内容只能是一列

~~~SQL
select * from 表1 where 字段1 in (selct 字段2 from 表2  where 条件);
~~~

## 数据库备份

在命令行中输入

### 备份

* 锁表
* 备份慢
* 不可以做增量备份
* 单线程

~~~SQl
mysqldump -u用户名 -p 数据库名称 >路径.sql      #备份数据库下的所有表
mysqldump -u用户名 -p 数据库名称  数据表>路径.sql       #备份单个表
mysqldump -u用户名 -p databases 数据库名称  数据表>路径.sql     #备份整个数据库
~~~

### 导入

~~~SQL
mysql -u用户名 -p数据库名称 < 库路径.sql
~~~

或者

~~~SQL
source [sql文件路径]
~~~

在sql下并切换到要还原的库下

### xtrabackup

* 多进程
* 支持增量备份
* 锁行
  
#### 安装

~~~shell

yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm #安装yum仓库

yum install percona-xtrabackup-24 #安装
~~~

#### 数据库创建用户

~~~SQL

mysql> create user 'backup'@'localhost' identified by 'backup';
Query OK, 0 rows affected (0.00 sec) 
创建用户

mysql> grant reload,lock tables,process,replication client on *.* to 'backup'@'localhost';
Query OK, 0 rows affected (0.00 sec)
设置用户重载、锁表、查看全部用户线程/连接、备份客户端权限

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
刷新用户配置
~~~

#### 全备份

~~~shell

xtrabackup --backup   --target-dir=备份的目录 -u用户名 -p密码 --socket=MySQL中的sock文件
~~~

##### 还原

~~~shell

准本文件
xtrabackup --prepare --target-dir=备份的目录

恢复部分文件
cd 备份的目录
cp -rf 需要复制的内容 MySQL路径
chown mysql.mysql 拷贝后的文件 -R

恢复全部文件
xtrabackup --copy-back --target-dir=备份路径
cd mysql路径
chown mysql.mysql * -R
~~~

#### 增量备份

~~~shell

xtrabackup --backup --target-dit=增量备份路径 --incremental-basedir=之前一次备份路径 -u用户名 -p密码 --socket=mysql的sock文件
~~~

#### 还原(要全部删除后才可以使用)

~~~shell
xtrabackup --prepare --apply-log-only --target-dir=全备份路径
xtrabackup --prepare --apply-log-only --target-dir=全备份路径 --incremental-dir=增量备份路径
xtrabackup --prepare --apply-log-only --target-dir=上一次全备份路径 --incremental-dir=新一次全备份路径
xtrabackup --copy-back --target-dir=全备份路径
cd mysql的路径
chown mysql.mysql * -R
systemctl restart mysqld
~~~

## 数据库主从

设置配置文件中
主机

~~~shell
server-id=1 设置id
log-bin=/mydata/log/master-bin 启动binlog日志
sync_binlog = 1 确保主从复制事务安全
~~~

备机

~~~shell
server-id =12 id不可一致
relay_log =/mydata/log/slave-log
sync_binlog = 1
read-only=ON
~~~

主机执行

~~~SQL
mysql> grant replication slave on *.* to 'slave'@'192.168.21.131' identified by '1234'; #配置一个远程登录用户
Query OK, 0 rows affected, 1 warning (0.00 sec)
mysql> flush privileges; #重新读取用户配置
Query OK, 0 rows affected (0.01 sec)
mysql> show master status\G #查看binlog日志内容
~~~

备机执行

~~~SQL

CHANGE MASTER TO
  MASTER_HOST='master2.example.com',
  MASTER_USER='replication',
  MASTER_PASSWORD='password',
  MASTER_PORT=3306,
  MASTER_LOG_FILE='master2-bin.001',
  MASTER_LOG_POS=4,
  MASTER_CONNECT_RETRY=10; #监控主服务器的时间
 连接主库
change master to master_host='192.168.21.128',master_user='slave',master_password='1234';
 启动进程
start slave；
 查看状态
show slave status\G
~~~

确认设置完成

~~~sql
在备机上执行
show slave status\G
存在
slave_io_running:yes
slave_sql_running:ye
~~~
