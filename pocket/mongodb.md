# Mongo

[toc]

## 软件操作

### 安装

~~~SHELL
sudo apt-get update     #跟新源
sudo apt-get install -y mongodb     #安装最新的稳定版本
~~~

### 查看

~~~SHELL
sudo systemctl status mongodb   #查看服务运行情况

mongo --eval 'db.runCommand({ connectionStatus: 1 })'     #查看软件的一些重要配置
~~~

### 管理

~~~SHELL
sudo systemctl status mongodb       #验证服务状态
sudo systemctl stop mongodb     #停止服务
sudo systemctl start mongodb        #启动服务
sudo systemctl restart mongodb      #重启服务
~~~

### 开机自启动

~~~SHELL
sudo systemctl disable mongodb      #关闭开机自启动
sudo systemctl enable mongodb       #开启开机自启动
~~~

## 数据库操作

### 进如操作界面

~~~SHELL
mongo
~~~

### 查看所有数据库

~~~SHELL
show dbs
~~~

mongodb不显示空数据库

### 创建数据库

~~~SHELL
use 数据库名
~~~

### 查看当前链接的库

~~~SHELL
db
~~~

### 删除

~~~SHELL
db.dropDatabase()       #删除当前链接的库
~~~

## 集合

~~~SHELL

~~~
