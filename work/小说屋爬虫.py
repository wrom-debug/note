

'''
针对小说屋 http://www.xiaoshuowu.com 的爬虫无任何反扒措施
1.访问首页,并解析出每个类别的名称和链接
2.访问每个类别的链接,并解析出第一页的全部小说名与对应的目录链接
2.2对下面步骤进行多线程处理
3.访问每个小说的目录,并解析出每个章节与对应的链接
4.访问每个章节,并解析出小说内容并存储到对应的小说.txt中
注意:将章节标题在内容开始单独成一行可以让手机阅读的软件自动分章节
'''

import random
import re
import threading
import time
import urllib.robotparser
import requests
from lxml import etree


def get_html(url):
    # get请求       输入url     返回网页的html源码
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    try:
        a=requests.get(url,headers=headers)
        if a.status_code==200:
            a.encoding=a.apparent_encoding

            return a.text
        else:
            return None
    except Exception as e :
        print(f"请求失败__原因{e}")
        return None

def write_in(c,son_catalogue):
    shumin=f'{son_catalogue[1]}.txt'
    with open(shumin,'a+',encoding='utf-8') as file:
        file.write(c+"\n")

def jx1(html):
    # 输入html存储到文件中
    with open(r'003-python知识\mb.html','w+',encoding='utf-8')as file:
        file.write(html)

def get_catalogue(url):
    # 解析首页      输入url    返回玄幻·魔法等标题的url与标题组成的元组列表
    html=get_html(url)
    try:
        html=etree.HTML(html)
        title_a=html.xpath('/html//div[contains(@class, "m_link")]/a')
        title={}
        for i in title_a:
            k=i.xpath('./text()')
            v=i.xpath('./@href')
            title[k[0]]=v[0]
        return title
    except:
        return "首页解析错误"

def get_novel_directory(url,i):
    # 解析分类页      输入url    返回该分类下的小说目录url与小说名组成的元组列表
    html=get_html(url)
    try:
        html=etree.HTML(html)
        title_div=html.xpath('//div[@id="jieqi_page_contents"]/div')
        title=[]
        for div in title_div:
            k=div.xpath('./div[2]/div[1]/a[1]/@href')
            v=div.xpath('./div[2]/div[1]/a[2]/text()')
            title.append([k[0],v[0]])
        #a=re.findall(r'class="c_subject"><a href="(.*?)".*?target="_blank">(.*?)<',html,re.S)
        return title
    except:
        return f'{i}解析错误'
        

def get_chapter(url):
    # 解析小说目录     输入url      返回该小说的章节url与章节名的元组列表
    html=get_html(url)
    if html != None:
        a=re.findall(r'<ul class="chapters">(.*?)</ul>',html,re.S)
        b=re.findall(r'href="(.*?)".*?>(.*?)<',a[0],re.S)
        return b
    else:
        return None

def get_content(url):
    # 解析内容      输入url        返回小说内容
    html=get_html(url)
    if html != None:
        a=re.findall(r'<div class="tishi">(.*?)<div class="tishi">',html,re.S)
        b=re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',a[0],re.S)
        return b
    else:
        return None
        
def threading_run(son_catalogue):
    # 多线程运行函数    导入有小说目录url与小说名组成元组去请求   获取小说全部内容
    novel_directory=get_chapter(son_catalogue[0])
    print(1)
    """
    f novel_directory != None:
        for i in range(len(novel_directory)):
            print(son_catalogue[1]+"---"+novel_directory[i][1]+">>>开始下载")
            content=get_content(novel_directory[i][0])
            if content != None:
                fiction=novel_directory[i][1]+"\n"+"\n".join(content)
                write_in(fiction,son_catalogue)
                print(son_catalogue[1]+"---"+novel_directory[i][1]+">>>下载完成")
    """
    
        
def main():
    url="http://www.xiaoshuowu.com"
    catalogue=get_catalogue(url)
    if catalogue != None:
        # for i in range(len(catalogue)):
        #     print(catalogue[i][1])
        #     son_catalogue=get_novel_directory(catalogue[i][0])
        #     if son_catalogue != None:
        #         for j in range(len(son_catalogue)):
        #             print(son_catalogue[j][1])
        #             novel_directory=get_chapter(son_catalogue[j][0])
        #             if novel_directory != None:
        #             for k in range(len(novel_directory)):
        #                 print(novel_directory[k][1])
        #                 content=get_content(novel_directory[k][0])
        #                 fiction="\n".join(content)
        #                 write_in(fiction,son_catalogue)
    
        print(catalogue[0][1])
        son_catalogue=get_novel_directory(catalogue[0][0])
        if son_catalogue != None:
            t1=threading.Thread(target=threading_run,args=(son_catalogue[0],))
            t1.start()
            t2=threading.Thread(target=threading_run,args=(son_catalogue[1],))
            t2.start()
            # t3=threading.Thread(target=threading_run,args=(son_catalogue[3],))
            # t3.start()
            t1.join()
            t2.join()
            # t3.join()
            print("整体结束")

def cs():
    url="http://www.xiaoshuowu.com"
    catalogue=get_catalogue(url)

    if type(catalogue)==dict:
        for i in catalogue.keys():
            son_catalogue=get_novel_directory(catalogue[i],i)
            if type(son_catalogue)==list:
                t1=threading.Thread(target=threading_run,args=(son_catalogue[0],))
                t1.start()
                t2=threading.Thread(target=threading_run,args=(son_catalogue[1],))
                t2.start()
                t1.join()
                t2.join()
                print("ok")
    
if __name__ == "__main__":
    #main()
    cs()
