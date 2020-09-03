# liunx基础使用

[toc]

## 基础

命令行构成:

~~~shell
用户@计算机名：路径$
普通用户$
root#
~~~

修改除home目录下以外的文件需要管理员身份运行(运行是需要输入管理员密码)

~~~shell
sudo 命令
~~~

ctrl+l键清空终端显示
ctrl+o执行一次再显示一次
ctrl+s 锁屏
ctrl+q解锁
ctrl+r搜索输入过的命令

命令|作用
---|:--:
echo |显示
type 命令 |查看命令是否是内部
alias 别名=“命令”|给命令创建别名（相当于宏）
cd|切换目录（可以使用绝对路径（/根目录下的路径）也可以使用相对路径（.代表当前目录  ..代表当前目录的上级目录））
ls    ls -l    ls -a|内容当前路径下的文件 -l 查看详细内容 -a 查看隐藏文件（以点开头的文件）
cp [-r]原文件 复制的路进|复制文件 [-r] 复制路径
vm 原文件 路径|移动文件
rm 文件|删除文件[-r]删除路径
mkdir 文件夹名称|创建文件夹[-p]创建路进下文件夹
rmdir 文件夹名称|删除空文件夹
touch 文件名称|创建文件
cat 文件名称|查看文件内容
tty |查看当前桌面号
echo $SHELL|查看当前shell的类型
cat /etc/shells |查看系统可用的shell
man 命令|查看命令手册
whatis 命令 |查看命令行支持的章节
whoami |查看当前登录用户
w|查看当前登录的用户，与其他信息
data|时间
shutdown|关机 一份分钟
poweroff |关机

查看之前执行的命令
~/.bash_history 或者 history
！命令 匹配最近一次输入

## 查看系统版本

~~~shell
cat /etc/issue
sudo lsb_release -a
~~~

## 软件管理

命令|作用
---|:--:
sudo apt- get update|更新软件包
sudo apt-get install 软件名称|安装软件
sudo apt-get remove --purge 软件名|卸载软件

## ssh服务

命令|作用
---|:--:
sudo service ssh start/restart/stop|启动/重启/停止ssh服务
ssh-keygen|生成ssh密钥对在用户下.ssh文件夹下（rsa的私钥 rsa.pub公钥）

## 解压
