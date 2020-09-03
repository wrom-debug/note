# git使用命令 {ignore}

[toc]

## 安装git

~~~shell
sudo apt-get install git
~~~

可以在命令行中输入git查看是否安装成功，成功会输出git手册

也可使用`git --version`查看git版本

## 初始化

配置名称和email

~~~shell
git config  --global user.name "用户名"
git config --global user.email "邮箱"
~~~

执行后会在工作目录下生成一个`.gitconfig`的文件

## 克隆网站上的库

克隆库到当前目录下

~~~shell
git clone   git@github…/https:github..
~~~

## 查看库状态

进入仓库主目录并输入：

~~~shell
git status
~~~

## 添加修改到暂存区

使用`git add 文件名称`命令跟踪此新建文件

使用`git rm --cached 文件名`或者`git reser -- 文件名`来撤销暂存去的修改

可以使用`git diff`查看跟踪的文件修改的情况

也可以使用`git diff --cached`查看暂存区的全部修改并按`q`退出

## 记录版本

每更新一个版本进行一次记录

~~~shell
git commit
~~~

在跳出的文件中写下更新的内容

## 上传到远程仓库

~~~shell
git push -u origin 分支名称（默认master）
~~~

## 更新本地仓库

~~~shell
git pull origin 分支名
~~~
