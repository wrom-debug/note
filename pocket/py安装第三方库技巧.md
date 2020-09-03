# 第三方库安装

[toc]

## 对与解决pip install 安装第三方库时出现Read timed out.的问题

* 由于pip install安装对连接外网的网速有一定要求所有需要是用代理
原：`pip install 所需的第三方库的名称`

改为：`pip install  --index-url https://pypi.douban.com/simple 所需的第三方库的名称`

即可解决

## 出现connection timeout

使用国内的镜像网站下载

`pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com packagename # packagename是要下载的包的名字`

`pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com --upgrade pip # 升级pip`

## pip的使用方法

`pip list`:可查看已经安装的第三方库

`pip list -o`:可查看可升级的第三方库

`pip --version`:可查看版本和路径

`pip install -U pip`:升级pip

`pip install SomePackage`:              最新版本

`pip install SomePackage==1.0.4`:        指定版本

`pip install 'SomePackage>=1.0.4'`:      最小版本

`pip install --upgrade SomePackage`:更新第三方库

`pip uninstall SomePackage`:卸载包
