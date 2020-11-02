# django {ignore}

[toc]

---

## web框架本质

使用socket简单实现web框架功能

~~~python

import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8001))
sk.listen()
conn,addr = sk.accept()
from_b_msg = conn.recv(1024)
str_msg = from_b_msg.decode('utf-8')
conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
conn.send(b'hello')
~~~

### http请求(request)格式

![http请求格式](img/2.jpg "http请求格式")

请求方式：

1. GET：    向指定的资源发出“显示”请求

2. HEAD：   与GET方法一样，都是向服务器发出指定资源的请求。只不过服务器将不传回资源的本文部分（只返回文件的head标签内的内容）

3. POST：    向指定资源提交数据，请求服务器进行处理（例如提交表单或上传文件）。传输的数据在请求文本中

4. PUT：    向指定资源位置上传其最新内容

5. DELETE： 请求服务器删除指定资源

6. TRACE：  回显服务器收到的请求，主要用于测试或诊断

7. OPTIONS：    这个方法可以使服务器传回该资源所支持的所有HTTP请求方法。用'*'来代替资源名称，向Web服务器发送OPTIONS请求，可以测试服务器功能是否正常运作。

8. CONNECT：    HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。通常用于SSL加密服务器的链接（经由非加密的HTTP代理服务器）。

示例：

~~~http

GET / HTTP/1.1
Host: 127.0.0.1:8001
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6
Cookie: csrftoken=wbpwiMbku4CIpXWMAb8KiTudh2gPKHC9eaMjnriN4fFSP6dcgRuXwS27GH3eYKtp
~~~

### http响应(response)格式

![http相应格式](img/3.jpg "http相应格式")

响应状态码

![响应状态码](img/4.png "响应状态码")

### URL

超文本传输协议（HTTP）的统一资源定位符将从因特网获取信息的五个基本元素包括在一个简单的地址中：

* 传输协议

* 层级URL标记符号(为[//],固定不变)

* 服务器。（通常为域名，有时为IP地址）

* 端口号。（以数字方式表示，若为HTTP的默认值“:80”可省略）

* 路径。（以“/”字符区别路径中的每一个目录名称）

* 查询。（GET模式的窗体参数，以“?”字符为起点，每个参数以“&”隔开，再以“=”分开参数名称与数据，通常以UTF8的URL编码，避开字符冲突的问题）

* 片段。以“#”字符为起点

以http://www.luffycity.com:80/news/index.html?id=250&page=1 为例, 其中：

http，是协议；
www.luffycity.com，是服务器；
80，是服务器上的默认网络端口号，默认不显示；
/news/index.html，是路径（URI：直接定位到对应的资源）；
?id=250&page=1，是查询。
大多数网页浏览器不要求用户输入网页中`http://`的部分，因为绝大多数网页内容是超文本传输协议文件。同样，“80”是超文本传输协议文件的常用端口号，因此一般也不必写明。一般来说用户只要键入统一资源定位符的一部分（www.luffycity.com:80/news/index.html?id=250&page=1)就可以了

### MVC与MTV

　Web服务器开发领域里著名的MVC模式，所谓MVC就是把Web应用分为模型(M)，控制器(C)和视图(V)三层，他们之间以一种插件式的、松耦合的方式连接在一起，模型负责业务对象与数据库的映射(ORM)，视图负责与用户的交互(页面)，控制器接受用户的输入调用模型和视图完成用户的请求，其示意图如下所示：

![MVC流程图](img/6.png "MVC流程图")

Django的MTV模式本质上和MVC是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，Django的MTV分别是值：

M 代表模型（Model）： 负责业务对象和数据库的关系映射(ORM)。
T 代表模板 (Template)：负责如何把页面展示给用户(html)。
V 代表视图（View）：   负责业务逻辑，并在适当时候调用Model和Template。
　　除了以上三层之外，还需要一个URL分发器，它的作用是将一个个URL的页面请求分发给不同的View处理，View再调用相应的Model和Template，MTV的响应模式如下所示：

![MTV流程图](img/7.png "MTV流程图")

## 安装django并配置使用

1. 安装jdango
   `pip install django==1.11.17`
\#注意1.11.9版本有bug

2. 创建一个django project
   `django-admin startproject mysite`   创建名为mysite的项目

3. 创建后的文件结构
![django文件结构](img/5.png "django文件结构")
manage.py --- django项目里的工具，通过它可以调用django shell和数据库，启动关闭项目与项目交互等，不管框架有几个文件，必然有一个启动文件。
settings.py --- 包含整个项目的默认设置，包含数据库信息，调试标志以及其他一些工作变量。
url.py --- 负责把URL模式映射到应用程序
wsgi.py --- runserver命令就是使用wsgiref模块做简单的web server，所有与socket相关的内容的在这个文件里。

4. 创建app
    在项目路径下输入`python manage.py startapp diyigeapp`
    并且在settings.py文件的INSTALLED_APPS中添加新生成的app中的apps.py的appconfig类名称(用于在django shell管理时可以查看app)

   ![添加新建app名称](img/8.png '添加新建app名称')

5. 创建存储模板文件
   在项目路径下创建一个文件夹存放模板文件，并在setting.py文件中添加`'DIRS': [os.path.join(BASE_DIR, '文件夹名称')]]`

   ![添加模板路径](img/9.png '添加模板文件夹路径')

6. 运行项目
   切换目录到项目路径下执行`python manage.py runserver 127.0.0.1:8080`

## RUL

url分配原则是由上到下依次匹配如果一项匹配上了就不再匹配下面的url，正则表达式只需写路径，前面的网站不需要写,但是最后要加上`/`符号结尾。

### 一般方式

~~~python

from django.conf.urls import url
from django.contrib import admin
from diyigeapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home),
]
~~~

url(正则表达式，app中的视图函数)

### 参数传递

可以将url中的内容传递给视图函数，无论用的是什么匹配方式传递给视图函数的都是字符串

#### 无名分组

~~~python
url.py
url(r'^home/(\d{4})/(\d{2})',views.home)

views.py
def home(request,year,moth):
   return HttpResponse(yes,moth)
~~~

在进行正则匹配时进行括号分组，即可将匹配的对应值传递给视图函数作为对应位置的参数

#### 有名分组

~~~python

url.py
url(r'^home/(?p<year>\d{4})/(?p<moth>\d{2})',views.home)

views.py
def home(request,moth,year):
   return HttpResponse(year,moth)
~~~

又名分组就是在正则匹配时对分组进行命名，在将匹配的分组向试图函数传递时只要注意分组名与型参名称一致就可以，不用注意型参位置

而外内容

~~~python

url.py
url(r'^home/',views.home,{'day':'21'})
~~~

会将21这个实参传递给视图函数的day型参

#### 设置参数默认值

~~~python

url.py
url(r'^home/(?p<year>\d{4})/(?p<moth>\d{2})',views.home))
url(r'^home/',views.home))

views.py
def home(request,moth=9,year=1997):
   return HttpResponse(year,moth)
~~~

设置参数默认值就是在视图函数中添加默认参数值

### URL分发(include)

项目路径下的url.py

~~~python

from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home),
    url(r'^app01/',include('app01.urls'))
]
~~~

app01下的urls.py

~~~python

from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
   url(r'^$', views.app01base),
   url(r'^index/', views.index),
]
~~~

url分发就是将app01匹配的内容再放到app01下的urls中进行匹配，app01下的urls路径就可以将之前的`^app01\`省略不写

### URL别名

## 视图

### 请求(request)相关属性方法

~~~python

views.py
def index(request):
   print(request.body)
   return redirect()
~~~

请求方法与属性：

1. request.schem: 请求协议

2. request.body:  请求报文主体(post传输方式)

3. request.path:  请求如路径(不包含域名)

4. request.path_info:   获取路径

5. request.get_full_path():   获取路径及参数

6. request.method:   请求方式(大写)

7. request.MATE： 请求头相关内容

8. request.GET:   类似字典，包含所有GET请求参数

9. request.POST:  与GET类似，上传的文件数据在FILES属性中

10. request.get_host():  获得域名ip与端口(多代理后失败)

11. request.is_ajax():  如果请求是ajax发送的就返回True

12. request.is_secure():   是否是https发起的

### 响应(response)相关属性方法

#### HttpResponse

~~~python

from django.http import HttpResponse
HttpResponse("ok")   #返回字符串
~~~

属性(可以读取与赋值)：

* content： 响应内容

* charset： 响应编码格式

* status_code:响应状态码

#### render

~~~python

from django.http import render

return rendrt(request,'模板路径',{传参字典})
~~~

返回一个网页文件或者模板，可以传递字典参数生成动态网页。

#### redirect

~~~python
from django.http import redirect

return redirect('跳转路径地址')
~~~

返回状态码30x进行跳转，让浏览器自动跳转。

redirect中还有一个参数permanent为Ture时为永久跳转，不填写就为临时跳转。

#### JsonRespose

~~~python

from django.http import JsonResponse
response = JsonResponse({'foo': 'bar'})
return response
~~~

返回json数据

### CBV与FBV

#### FBV函数方式处理视图

~~~python

from django.http import HttpResponse

def when(fun):
   def whens(*args,**kwargs):
      start=time.time()
      ret=fun(*args,**kwargs)
      end=time.time()
      return ret
   return whens
@when
def my_view(request):
   if request.method == 'GET':
      return HttpResponse('OK')
   if request.method == 'POST'
      return HttpResponse('no')
~~~

FBV就是正常的函数编程添加装饰器也是普通操作

#### CBV类方式处理函数

~~~python

views.py
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator

def when(fun):
   def whens(*args,**kwargs):
      start=time.time()
      ret=fun(*args,**kwargs)
      end=time.time()
      return ret
   return whens
@method_decorator(when,name="get")  #方法三
class MyView(View):

      def dispatch(self,request,*args,**kwargs):
         start=time.time()
         ret=super().dispatch(request,*args,**kwargs)
         end=time.time()
         return ret
         #方式一
      @method_decorator(when) #方法二
      def get(self, request):
            return HttpResponse('OK')

      def post(self,request):
            return HttpResponse("ok")
url.py
url(r'^abb/',views.abb.as_view()),
~~~

使用cbv方式写视图函数在url中要使用`类.as_view()`方法调用，可以在`as_view(类属性=“”)`方式来进行赋值。方法传参方式与FBV一致。

vbc实际过程是，匹配url，调用as_view()方法，再调用里面的viwe方法，再调用dispatch方法。使用其中的

~~~python

if request.method.lower() in self.http_method_names:  #判断请求方式是否在默认方式中
   handler = getattr(self, request.method.lower(), self.http_method_not_allowed) #handler=实例化对象.求情方式小写的方法的对象
   #在调用hadler()就可以实现各种请求的对应方法的执行
~~~

## 模板

使用`{{}}`包裹变量

使用`{%%}`包裹逻辑

### 变量

~~~python

模板html

{{num}}
{{a.2}}
{{c.name}}
{{c.run}}

viwes.py

def index(request):
   num=50
   a=[10,20,30]
   class go():
      def __init__(self):
         self.name='123'
      def run(self):
         return 'ok'
   g=a()
   return render(request,"home.html",{'num':num,'a':a,'c':g})
   #可以在第三个返回值使用locals(),会返回函数内部所有变量以{'变量名':变量值,...}形式的字典
~~~

django中如果变量属性名与方法重复会执行属性，及属性优先级比方法高。

#### 过滤器

使用方法`{{变量|过滤器}}`

过滤器|说明
|---|---
|length|数据长度
|default:“默认字符”|如果变量为空或者false，就显示默认字符
|filesizeformat|将数值显示可读取的大小‘4.1 MB’这样
|slice:'0:4'|切片
|date:'y-m-d'|时间格式化
|tuncatechars:'9'|字符省略（加上三点一共的字符）
|tuncatewords:'3'|单词省略（显示3个单词）
|cut：‘指定字符’|删除字符串中所有指定字符
|join：“指定字符”|使用指定字符连接列表中所有元素
|safe|将字符串识别成标签

### 标签(逻辑)

#### for循环标签

~~~html

{% for i in a %}
   {{forloop.counter}}
   <h1>哈哈</h1>
{% empty %} #循环为空时执行
   <h2>ccc</h2>
{% endfor %}
~~~

##### for其他方法

|变量|说明
|--|--
|forloop.counter|当前索引值(从1开始)
|forloop.counter0|当前索引值(从0开始)
|forloop.revcounter|当前索引值的倒叙(从1开始)
|forloop.revcounter0|当前索引值的和倒叙(从0开始)
|forloop.first|如果当前循环是第一次循环就为Tuer
|forloop.last|如果当前循环是最后一次循环就为Tuer
|forloop.parentloop|外层循环可以是使用上面的方法

#### if标签

~~~html

{% if a == b %}
   <h1>aaa</h1>
{% elif a == c %}
   <h2>bb</h2>
{% else %}
   <h3>cc</h3>
{% endif %}
~~~

不支持连续判断

#### with标签

~~~html

{% with a.c.b.5 as ash %}  #给复杂变量取别名

或者{% with ash=a.c.b.5 %}
   {{ash}}
{% endwith %}
~~~

#### csrf_token

~~~html

<form action="" method="post">
  {% csrf_token %}
</form>
~~~

django存在post校验，使用每次生成的form表单中添加随即值的键值对，与提交的数据判断。

#### 注释

~~~html

{#注释内容#}
~~~

### 自定义标签与过滤器

1. 将app添加到setting中[创建app](#安装django并配置使用)

2. 在app中创建templatetags文件夹

3. 在templatetags文件中创建`任意名称.py`文件并写以下内容

~~~python
from django import template
from django.utils.safestring import mark_safe

register = template.Library()   #register的名字是固定的,不可改变

@register.filter  #自定义过滤器
def filter_multi(v1,v2):   #过滤器必须会传递一个参数
    return  v1 * v2

//{{x|filter_multi:v2}}// #x=v1,v2=v2

@register.simple_tag  #自定义一个标签
def simple_tag_multi(v1,v2):
    return  v1 * v2

@register.inclusion_tag('result.html')  #将下方函数返回值传递给result.html进行渲染，并将渲染后的界面作为组件返回
def show_results(n):
    data=“1”
    return {"data": data}
~~~

模板中使用

~~~html

{% load emplatetags文件夹中文件名 %}
{{变量|过滤器名：过滤器传递参数}}   #至多两个参数

~~~

### 模板继承

~~~html

父模板
内容1
{% block 钩子名称 %}
   内容2
{% endblock %}
内容3

子模板
{% extends "户模板文件名" %}
{% block 父模板钩子名 %}
   内容4
{% endblock %}
~~~

由于大部分模板框架类似就可以在父模板中添加钩子，来替换钩子中的`内容2`生成新的子模板。不过子模板要在一开始使用`{% extends “父模板文件名" %}`指定子模板继承的父模板。

### 组件

~~~html

插入组件模板
内容1
{% include "完整功能组件" %}
内容2
~~~

组件就是在模板中将完整功能的html文件插入
组件是提供某一完整功能的模块，如：编辑器组件，QQ空间提供的关注组件等。
而插件更倾向封闭某一功能方法的函数。

## 静态文件

1. 在项目路径下创建任意名的静态文件存储文件夹

2. 并在setting中设置`STATC_URL='/static/'`此项设置静态文件别名

3. 并添加`STATICFILES_DIRS = [os.path.join(BASE_DIR,'静态文件名称‘)]`该内容

~~~html

{% load 静态文件别名 %}
<img src="/静态文件别名/具体资源">
<img src="{% 静态文件别名 具体资源 %}">
<img src={% get_static_prefix %}具体资源>   #{% get_static_prefix %}返回/别名/
~~~
