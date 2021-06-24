# Mongo

[toc]

## 软件操作

### 安装

~~~shell
sudo apt-get update     #跟新源
sudo apt-get install -y mongodb     #安装最新的稳定版本
~~~

### 查看

~~~shell
sudo systemctl status mongodb   #查看服务运行情况

mongo --eval 'db.runCommand({ connectionStatus: 1 })'     #查看软件的一些重要配置
~~~

### 管理

~~~shell
sudo systemctl status mongodb       #验证服务状态
sudo systemctl stop mongodb     #停止服务
sudo systemctl start mongodb        #启动服务
sudo systemctl restart mongodb      #重启服务
~~~

### 开机自启动

~~~shell
sudo systemctl disable mongodb      #关闭开机自启动
sudo systemctl enable mongodb       #开启开机自启动
~~~

## 数据库操作

### 进如操作界面

~~~shell
mongo   
~~~

### 查看所有数据库

~~~shell
show dbs    #查看所有数据库简写
show databases  #查看所有数据库
~~~

mongodb不显示空数据库

### 创建数据库

~~~shell

use 数据库名    #切换数据库，如果不存在那么就在内存中创建
~~~

### 查看当前链接的库

~~~shell

db  #显示当前的数据库
~~~

### 删除数据库

~~~shell

db.dropDatabase()       #删除当前链接的库
~~~

## 表/集合

### 创建

~~~shell

db.表名称   #没有就在内存中创建
db.createCollection("表名称")   #在硬盘中创建表
~~~

### 查

~~~shell

show tables #查看当前数据库所有硬盘中的表
~~~

### 删

~~~shell

db.表名.drop()  #删除当前数据库中的表
~~~

## 数据

- ObjectID：Documents 自生成的 _id(主键)
- String：字符串，编码格式必须是utf-8
- Boolean：布尔值，true 或者false (Python中 True False 首字母大写)
- Integer：整数 (Int32 Int64 你们就知道有个Int就行了,一般我们用Int32)
- Double：浮点数 (没有float类型,所有小数都是Double)
- Arrays：数组或者列表，多个值存储到一个键就是Python中的字典
- Null：空数据类型 , 一个特殊的概念,None Null
- Timestamp：时间戳
- Date：存储当前日期或时间unix时间格式 (我们一般不用这个Date类型,时间戳可以秒杀一切时间类型)

## 记录

### 增加

~~~shell

插入：

db.表名.insert(数据)
db.表名.insert({name:"沙悟净",age:66.666,hobby:[1,2,3,4,5]})

官方推荐：
db.user.insertOne({}) #增加一条数据
db.user.insertMany([{},{}]) #批量增加数据

保存：

db.user.save({})    #可以保存一条新的记录或者对久记录进行更新保存
~~~

### 查询

~~~shell

db.user.find({name:"沙悟净"})    #查找所有符合条件的记录
db.user.findOne({name:"沙悟净",age:66.666}) #返回符合条件中的第一条记录

db.post.find().pretty() #以缩进格式显示记录
~~~

#### 查询条件逻辑

~~~shell

ADN:
db.user.find({name:"沙悟净",age:66.666})
db.users.find({$and:[{"k1":1},{"k2":2}]})   #使用{$and:[{条件1},{条件2}]}，且条件中键要要使用""引起

OR:
db.user.find({$or:[{条件1},{条件2}]})   #与and一样键需要""引起

db.user.find({name:"沙悟净",age:{$比较符:值}})  #只有数值值为数值时才可以使用

db.user.find({age:{$in:[值1,值2]}}) #匹配实际值在后面列表元素的记录，值是列表时有条件值就匹配
db.user.find({hobby:{$all:[值1,值2]}})  #只有值是列表时可用，条件是列表的子集
~~~

比较符：

- gt:大于
- lt:小于
- gte:大于等于
- lte:小于等于
- eq:等于
- ne:不等于

### 删除

~~~shell

db.表名.remove({})  #删除所有匹配的记录

官方推荐：
db.user.deleteOne({})   #删除匹配的第一个记录
db.user.deleteMany({})  #删除所有匹配的记录
~~~

### 修改

~~~shell

db.user.update({条件},{$修改器:{修改值}})   #修改所有匹配的记录值

官方推荐：
db.user.updateOne({条件},{$修改器:{修改值}})    #修改匹配的第一条记录
db.user.updateMany({条件},{$修改器:{修改值}})   #修改所有匹配的记录值
~~~

修改器：

- set:设置值，如果没有该字段就创建该字段
- unset:删除字段 `{字段:1}`

- inc:数值引用增加 `{字段:-1/1}`

- push:列表追加一个元素 `{hobby:1}`
- pull:列表删除一个元素 `{hobby：1}`
- pop:删除列表中第一个(1)或的最后一个(-1)  `{hobby:-1/1}`
- pushAll:列表批量追加  `{hobby:[1,2,3]}`
- pullAll:列表批量删除  `{hobby:[1,2,3]}`

### 排序、忽略、选取

~~~shell

db.user.find({}).sort({age:-1})  #排序倒序(-1)/正序(1)
db.user.find({}).skip(5)    #忽略前5条
db.user.find({}).limit(5)   #选取5条
~~~

如果上面3条都在同一条命令行中不论前后顺序，永远是先排序再忽略再选取

## python调用

### 安装库

~~~shell

pip install pymongo
pip3 install pymongo
~~~

### 调用

~~~python

from  pymongo import MongoClient
from bson.objectid import ObjectId  #引入ObjectId类
from pymongo import ASCENDING,DESCENDING    #引入排序正序与倒序
mc=MongoClient("127.0.0.1",27017)   #创建客户端链接并指定ip与端口
db=mcp['test']  #选择数据库或者创建

db.user.insert_one(字典)    #插入数据并返回数据的ObjectId
db.user.insert_many(列表)   #插入多条数据并返回数据的ObjectId列表

db.user.find({})    #查找并返回记录列表
db.user.find_one({})    #查找第一条记录并返回

db.user.update_one({},{})   #更新一条数据
db.user.update_many({},{})  #更新多条数据

db.user.delete_one({"_id":ObjectId("ID编号")})  #删除一条数据

db.player.find({}).limit(2).skip(2).sort("_id",DESCENDING)  #排序、选取、忽略
~~~

ObjectId不可以转json，但可以转字符串
