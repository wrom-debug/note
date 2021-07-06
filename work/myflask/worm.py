import requests 

from pymongo import MongoClient
from lxml import etree
import re
from lxml.etree import XPath
import multiprocessing



# for i in range(10):
#     pool.apply_async(func,(i,))
# pool.close()
# pool.join()
# print("end")
pool=multiprocessing.Pool(processes=4)
mc=MongoClient("127.0.0.1",27017)
db=mc['xs']
url="http://www.xiaoshuowu.com"

def get_html(url):
    # get请求       输入url     返回网页的html源码
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    try:
        a=requests.get(url,headers=headers)
        if a.status_code==200:
            a.encoding=a.apparent_encoding
            return a.text
        else:
            print(f"请求失败")
    except Exception as e :
        print(f"请求失败__原因{e}")
        return None

def xs_crea(title,name,aouthor,time):
    gs={'name':name,'key':[{'author':aouthor},{'time':time},{'data':[]}]}
    a=db[title].insert_one(gs)


def xs_save(title,name,aouthor,time,data):
    a=db[title].update_one({'name':name},{'$set':{'data':data}})
    a=db[title].update_one({'name':name},{'$set':{'time':time}})

def xs_db(jg):
    title=jg["title"]
    name=jg["name"]
    aouthor=jg["aouthor"]
    time=jg["time"]
    data=jg["data"]
    # print(db[title].find_one({'name':name}))
    if db[title].find_one({'name':name}):
        print("no*")
        xs_save(title,name,aouthor,time,data)
    else:
        print("*")
        xs_crea(title,name,aouthor,time)
        xs_save(title,name,aouthor,time,data)

def cs_resolver(a):
    with open('a.html',"w") as f:
        f.write(a)


def xs_top():
    # [{titlei:""，url：‘’}，{titlei:""，url：‘’}]
    global url
    html=get_html(url)
    html=etree.HTML(html)
    data=[]
    a=html.xpath('/html//div[4]/a')
    for i in a:
        # print(etree.tostring(i).decode("utf-8"))
        title=i.xpath('./text()')
        url=i.xpath('./@href')
        data.append({'title':title[0],'url':url[0]})
    # print(data)
    return data

def xs_title(d):
    # [{小说名：“”，作者：“”，url：“”,tiem：“”}]
    url=d.get("url")
    title=d.get("title")
    html=get_html(url)
    # cs_resolver(html)
    html=etree.HTML(html)
    data=[]
    div=html.xpath('//div[contains(@class,"c_row")]')
    # print(len(div))
    for i in div:
        # print(etree.tostring(i).decode("gbk"))
        d["name"]=i.xpath('./div[2]//a[2]/text()')[0]
        d["url"]=i.xpath('./div[2]//a[1]/@href')[0]
        d["aouthor"]=i.xpath('.//span[@class="c_value"][1]/text()')[0]
        d["time"]=i.xpath('.//span[@class="c_value"][3]/text()')[0]
        data.append(d)
    # print(title,len(data))

    return data

def xs_chapter(d):
    url=d.get("url")
    html=get_html(url)
    # cs_resolver(html)
    html=etree.HTML(html)
    ul=html.xpath('//div[3]/div/div[3]/ul//li')
    # print(url,len(ul))
    data=[]    
    for i in ul:
        chapter=i.xpath('./a/text()')[0]
        url=i.xpath('./a/@href')[0]
        data.append({"chapter":chapter,"url":url})
    return data

def xs_data(d):
    url=d.get("url")
    chapter=d.get("chapter")
    html=get_html(url)
    # cs_resolver(html)
    a=re.findall(r'<div class="tishi">(.*?)<div class="tishi">',html,re.S)
    b=re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',a[0],re.S)
    b="".join(b)
        
    return {"chapter":chapter,"plot":b}


def main():
    title_list=xs_top()
    l=len(title_list)
    t=[]
    # global pool
    for i in range(l):
        c=xs_title(title_list[i])
        for f in c:
            f["data"]=[] 
            #{'title': '玄幻·魔法', 'url': 'http://www.xiaoshuowu.com/html/864/864933/', 'name': '腹黑王爷傲娇徒', 'aouthor': '木夕熙', 'time': '21-07-03'}
            g=xs_chapter(f)
            for h in g:
                print(f["name"],h["chapter"],"开始下载")
                # {'chapter': '第001章 在下孤北辰', 'url': ''}
                j=xs_data(h)
                # {'chapter': '第001章 在下孤北辰', 'plot': ''}
                f['data'].append(j)
                print(f["name"],h["chapter"],"完成下载")
            xs_db(f)
            print(f["name"],"写入数据库")
                
            
    
def cs_xs_db():
    pass
    # title="类型"
    # name="小说名"
    # aouthor="作者"
    # data=[{章节：“”，内容：“”}]
    # time="时间"
    # xs_db(title,name,aouthor,time,data)
    # print(db[title].find_one())


if __name__ == "__main__":
    main()
    