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

### 镜像导出

`docker save -o 保存文件 镜像名称`

`docker ssave 镜像名称 > 保存文件`

### 导入镜像

`docker load -i 文件名称`

`docker load < 文件名称`

### 构建镜像

`docker bulid -t 镜像名称：标签 -f dockerfile 上下问路径`

#### docker-file

~~~shell

FROM mycentos  # 指定基础镜像
COPY epel.repo /etc/yum.repos.d/ # 复制文件
RUN  yum install -y nginx  # 运行命令
RUN  mdkir /data/html #多个run应该使用&&连接减少无意义层数
RUN  echo 'mynginx' > /data/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf #只复制
ADD # 复制并解压压缩包
ENV  alex=alexdsb   # 设置环境变量
ENV  wulaoban=dsb
WORKDIR /data/html  # 设置工作目录，exec进入之后直接进入的目录
USER root：root #指定用户与用户组
EXPOSE 80 # 设置端口
VOLUME # 指定容器的目录和运行是`-v`选项功能一致
CMD /bin/bash -c systemctl start nginx # 运行命令，cmd是运行镜像时执行的命令，RUN是bulid执行
cmd ["命令","选项","参数"]=cmd 命令 选项 参数
~~~

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
* 将物理目录挂载到虚拟目录上 `-v 物理路径：虚拟路径`
* 给容器起名称 `--name 新名称`

### 查看容器

`docker ps`

查看容器列表

* 查看所有 `-a`
* 查看id `-q`

`docker port 容器id|容器名称`
查看容器端口映射关系

`docker log 容器id|容器名称`
查看容器日志

* 实时输出 `-f`

`docker stats 容器id|容器名称`
查看容器状态

### 停止或开启容器

`docker stop 容器id|容器名称`
停止指定容器
`docker start 容器id|容器名称`
开起指定容器

### 进入容器

`docker exec -it 容器id|容器名称 shell路径`
exec进入后退出容器不会停止容器

### 删除容器

`docker rm 容器id|容器名称`

* 删除容器时如果容器正在运行是删除不了的需要强制删除 `-f`

`doker container prune`
删除所有停止的容器

### 容器导出成镜像

`docker commit 容器id|名称 镜像名称：版本`

* 说明 `-m`
* 创建时停止容器 `=p`
* 提交作者 `-a`

### 创建容器网络

`docker network create -d bridge test-net`

* 指定网络类型：bridge、overlay（用于swarm mod） `-d`

### 链接容器

~~~shell

docker run --name s1 --network test-net 镜像名称  #创建容器1
docker run --name s2 --network test-net 镜像名称  #创建容器2
~~~

容器1内部

~~~shell

ping s2
~~~

## 仓库

存放镜像的地方，包括公共仓库、私有仓库

### 远程仓库(dockerhub)

~~~shell

docker login  #登录dockerhub账户  
docker tag 源镜像名称 用户名/镜像名称 #修改镜像名
docker push 用户名/镜像名称 #上传
docker logout #登出
~~~

### 本地仓库

~~~shell

docker run -p 5000:5000 -d -v /opt/data/registry:/var/lib/registry registry #使用https协议
docker tag 源镜像名称 127.0.0.1：5000/镜像名称  #修改镜像名称
docker push 127.0.0.1：5000/镜像名称  #上传
访问127.0.0.1：5000/v2/_catalog 会输出上传的所有镜像
~~~

### 局域网

在局域网中启动一台先启动本地仓库，局域网中主机都在docker加速器中配置

`/etc/docker/daemon.json`

~~~shell

{
    "registry-mirrors": [
        "https://1nj0zren.mirror.aliyuncs.com",
        "https://docker.mirrors.ustc.edu.cn",
        "http://f1361db2.m.daocloud.io",
        "https://registry.docker-cn.com"
    ],
 "insecure-registries": [
    "192.168.21.128:5000" #对应的主机与端口
  ]

}
~~~

## 集群
