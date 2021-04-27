# docker

[toc]

## 安装

~~~shell

cd /etc/yum.repos.d/
wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum install -y docker-ce    #社区版 docker-ee 商业版
~~~

### 配置加速

由于dockerhub服务器在国外，需要配置docker加速器

配置`/etc/docker/daemon.json`如下：

~~~shell

{
    "registry-mirrors": [
        "https://1nj0zren.mirror.aliyuncs.com",
        "https://docker.mirrors.ustc.edu.cn",
        "http://f1361db2.m.daocloud.io",
        "https://registry.docker-cn.com"
    ]
}
~~~

运行`systemctl daemon-reload`、`systemctl restart docker`使加速器生效

## 镜像

类似系统的ios镜像文件

### 查找镜像

`docker seach 镜像名称`

~~~shell

NAME     DESCRIPTION                                   STARS        OFFICIAL            
mysql    MySQL is a widely used, open-source relation…   8560                [OK]                
name 名字
DESCRIPTION  描述信息
STARS 点赞数
OFFICIAL 是否是官方提供
~~~

### 查看镜像

`docker images`

~~~shell

REPOSITORY：表示镜像的仓库源

TAG：镜像的标签

IMAGE ID：镜像ID

CREATED：镜像创建时间

SIZE：镜像大小
~~~

* 显示镜像id `-q`
* 列出部分镜像 `docker image 镜像名称`

### 删除镜像

`docekr rmi 镜像名称|镜像id`

### 下载镜像

`docker pull 镜像名称`

## 容器

启动后的镜像

### 启动容器

`docker run 镜像`

会先查找本地是否处在镜像，如果不存在则去下载，下载后再去运行

* 创建一个虚拟终端 `-t`
* 交互式操作,一般与`-t`一同使用 `-i`
* 再使用`-it`参数后需要在镜像后添加一个shell的终端一般使用 `\bin\bash`
* 退出容器 `exit`或者`ctrl+d`
* 后台运行 `-d`
* 关联物理端口与虚拟端口关系 `-p 物理端口：虚拟端口`
  * 也可以关联指定ip端口，本机端口如果不写代表本机任意端口 `-p ip:端口：端口`
* 自动关联物理端口到虚拟端口 `-P`

### 查看容器

`docker ps`

* 查看所有 `-a`
* 查看id `-q`

### 停止或开启容器

`docker stop 容器id|容器名称`

`docker start 容器id|容器名称`

### 进入容器

`docker exec -it 容器id|容器名称 shell路径`

## 仓库

存放镜像的地方，包括公共仓库、私有仓库
