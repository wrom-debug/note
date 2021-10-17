import json
import requests 
from pymongo import MongoClient, mongo_client
from lxml import etree
import os
import uuid
from lxml.etree import XPath

HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
URL_HOME="https://www.foxnews.com"
#通过分析网页获得这个网页新闻获取api，一次最多获取文章数量位30条
URL="https://www.foxnews.com/api/article-search?searchBy=categories&values=fox-news/%s&size=%d&from=%d"
CLASSIFIER=['us','politics',]   #目前只测试过这两个类
""" 
返回json内容解析
[
    {
        "imageUrl": "图片url",
        "title": "新闻标题",
        "description": "首段内容",
        "url": "详细内容url",
        "publicationDate": "编辑时间",
        "lastPublishedDate": "最后发布时间",
        "category": {
            "name": "类型",
            "url": "类型对应url"
        },
        "isBreaking": false,
        "isLive": false,
        "duration": ""
    }
]
"""

mc=MongoClient("127.0.0.1",27017)
db=mc['foxnews']

def get_html(url):
    # get请求       输入url     返回响应
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    try:
        a=requests.get(url,headers=headers)
        if a.status_code==200:
            a.encoding=a.apparent_encoding
            return a
        else:
            print(f"请求失败")
    except Exception as e :
        print(f"请求失败__原因{e}")
        return None

def cs_resolver(data,classifier,num,i):
    #json数据存储
    with open(f'./json/{classifier}_{i}_{num}.json',"a+") as f:
        f.write(json.dumps(data.json()))

def img_save(data):
    # 图片存储
    uuid_str=str(uuid.uuid4())
    with open(f'./img/{uuid_str}.jpg',"wb") as f:
        f.write(data.content)
    return uuid_str

def new_db(data,classifier):
    # 数据库存储
    db[classifier].insert_one(data)

def author_xpath(data):
    #解析获取作者
    html=etree.HTML(data)
    author="".join(html.xpath('//div[@id="wrapper"]/div[2]//div[@class="author-byline"]//text()'))
    # print(author.rstrip())    
    return author.rstrip()

def new_xpath(data):
    # 解析获取正文
    contents=[]
    html=etree.HTML(data)
    data=html.xpath('//div[@id="wrapper"]/div[2]//div[@class="article-body"]/p')
    for p in data:
        content=p.xpath('./text()')
        content="".join(content)
        contents.append(content)
    re="\n".join(contents)
    return re    

def deal(classifier,data):
    # 数据结构存储
    for d in data:
        # print(type(d))
        
        img_url=d.get("imageUrl")
        img=get_html(img_url)
        
        uuid=img_save(img)
        d["imageUrl"]=uuid
        new_url=URL_HOME+d.get("url")
        new=get_html(new_url)
        d["contents"]=new_xpath(new.text)
        d["author"]=author_xpath(new.text)
        new_db(d,classifier)
        

def mian(classifier,num):
    # 主函数
    c =num %10
    n =num //10
    # print(n,c)
    if not os.path.exists('./img'):
        os.makedirs("./img")
    if not os.path.exists('./json'):
        os.makedirs("./json")
    if n!=0:
        for i in range(0,n*10,10):
            print(i)
            data=get_html(URL%(classifier,10,i))    
            cs_resolver(data,classifier,10,i)
            deal(classifier,data.json())
    if c!= 0:
        for i in range(n*10,num):
            print(i)
            data=get_html(URL%(classifier,1,i))    
            cs_resolver(data,classifier,1,i)   
            deal(classifier,data.json())
    

if __name__ == '__main__':

    classifier=CLASSIFIER[0] #需要的类型
    num=25 #需要多少条*10
    mian(classifier,num)    

