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

## 简单示例

~~~shell

scrapy startproject porname #创建工程
cd porname  #进入工程文件
scrapy genspider spidername www.baidu.com   #创建爬虫文件   一个工程会存在多个爬虫
scrapy crawl spidername #运行爬虫
~~~

### 爬虫文件

~~~python


import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ASA"    #爬虫名称
    allowed_domains = ['quotes.toscrape.com']   #请求允许范围，除初始请求外后续请求需要在这个域名下。不然会被过滤并提示错误
    start_urls = [  #启动爬虫是发起的请求地址，并将响应交由parse方法处理
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    #也可以使用start_requests方法构建初始请求
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):  #初始请求的响应，调用这个方法，可以通过传递的response参数提取数据，并提交item与request。
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)  #response.body可以获得响应的二进制数据
~~~

### item

item是定义爬取数据结构的类，使用方法类似字典，一旦定义了关键字就不能在使用时创建新的关键字。

~~~python

import scrapy


class TutorialItem(scrapy.Item):    
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QuoteItem(scrapy.Item):   #定义的item类必须继承scrapy.item类
    name = scrapy.Field()   #定义需要爬取的数据内容并使用scrapy.Field()占位
    num = scrapy.Field()
~~~

#### item的使用

spider中：

~~~python

import scrapy
from tutorial.items import QuoteItem    #导入对应的item类
from scrapy import Selector


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print("开始播放")
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()  #初始化item类
            item["name"] = quote.css('.text::text').extract_first() #往item的关键字中输入数据
            yield item  #提交item给pipelines进行存储操作。
        next = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next)
        # yield scrapy.Request(url=url, callback=self.parse)
~~~

pipeline中

~~~python
from itemadapter import ItemAdapter


class TutorialPipeline: #还有open_spider(当spider开始时调用)和close_spider(当spider关闭时调用)两个方法，两个方法的参数都是(self,spider)
    def process_item(self, item, spider):   #可以通过参数获得item和spider，对item进行存储操作
        # print(item)
        return item
~~~

## response

~~~python

from scrapy import Selector
body= ' <html><head><title>Hello World</title></head><body></body> </html>'
selector = Selector(text=body)  #可以通过str生成选择器对象，和response对象一样
title = selector.xpath(' //title/text () ’ ) .extract_first()
print(title)
~~~

- response.xpath("xpath匹配语句")
  - .get()/extract_first()    #获取一个匹配对象
  - .getall()/extract()   #获取多个匹配对象列表
- response.css("css选择器")
  - .get()/extract_first()    #获取一个匹配对象
  - .getall()/extract()   #获取多个匹配对象列表
  - .re("re匹配语句") #获取多个再匹配正则的对象列表
  - .re_first("re匹配语句") #获取一个再匹配正则的对象列表
  