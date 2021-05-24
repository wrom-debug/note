# scrapy

---
[toc]

## 安装

~~~shell

pip install scrapy
pip3 install scrapy
~~~

## 项目结构

~~~shell

.
├── scrapy.cfg
└── xiaoshuowu
    ├── __init__.py
    ├── items.py    #定义存储数据
    ├── middlewares.py  #中间件，有下载中间件和爬虫中间件
    ├── pipelines.py    #定义管道
    ├── settings.py #配置文件
    └── spiders #爬虫文件夹
        └── __init__.py      
~~~

## 创建工程

~~~shell

scrapy startproject porname #创建工程
cd porname  #进入工程文件
scrapy genspider spidername www.baidu.com   #创建爬虫文件
scrapy crawl spidername #运行爬虫
~~~
