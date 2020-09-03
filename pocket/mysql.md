# SQL

[toc]

## 安装myqsl

~~~SHELL
sudo apt-get install mysql-server
sudo apt-get install mysql-client
~~~

可以在/etc/mysql/debian.cnf中查看默认账户密码

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

### 修改默认帐号和密码

~~~SQL
mysql> update mysql.user set authentication_string=password('new passwd') where user='root' and Host ='localhost';
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
shuow create database wormdb;
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

~~~SQ;
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
