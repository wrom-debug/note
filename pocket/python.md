# python 虚拟化

## 安装虚拟环境包

~~~shell
pip3 install virtualenv
~~~

## 创建虚拟环境

在当前路径下创建虚拟环境

~~~shell
virtyalenv 新环境名称
--no-site-packages 不使用本地包
--python 指定python.exe文件
~~~

## 进入虚拟环境

linux

~~~shell

source 环境名/bin/activate
~~~

windows10

~~~shell

.\环境名\Scripts\activate.bat
~~~

## 退出虚拟环境

linux

~~~shell

deactivate
~~~

windows 10

~~~shell

.\环境名\Scripts\deactivate.bat
~~~

## 删除环境

删除`新环境`文件夹

## 使用新环境

和正常使用python一样

## 安装多包

~~~shell

在windows上执行如下命令：
将windows上安装的包做快照
pip freeze > requirement.txt
将requirement.txt发送到linux上
切换虚拟机
pip install -r requirement.txt -i https://pypi.douban.com/simple
~~~

## 虚拟环境管理

~~~shell

1. 安装
pip3 install virtualenvwrapper -i https://pypi.douban.com/simple
2.修改文件
vim ~/.bashrc
export WORKON_HOME=/envdir  
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'   
export VIRTUALENVWRAPPER_PYTHON=/opt/python36/bin/python3      
source /opt/python36/bin/virtualenvwrapper.sh 
3. 加载~/.bashrc
source ~/.bashrc
4.创建环境
mkvirtualenv django11 创建并切换
5.进入虚拟环境
workon name
6.切换到当前虚拟环境的文件夹
cdvirtualenv
7.切换到当前虚拟环境的第三方包的文件夹
cdsitepackages
8.退出
deactivate
9.列出当前管理的虚拟环境
lsvirtualenv
10.列出当前虚拟环境的第三方包
lssitepackages
11.删除虚拟环境
rmvirtualenv 必须要退出才能删除
~~~
