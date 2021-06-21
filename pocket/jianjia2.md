# jianjia2

## 变量

flask视图函数中

~~~python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 往模板中传入的数据
    my_str = 'Hello Word'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('hello.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                           )
~~~

在摸板文件中

~~~html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
  我的模板html内容
  <br />{{ my_str }}    <!-- hello word-->
  <br />{{ my_int }}    <!-- 10-->
  <br />{{ my_array }}  <!-- [3,4,2,1,7,9]-->
  <br />{{ my_dict }}   <!-- {'name': 'xiaoming', 'age': 18}-->
</body>
</html>
~~~

变量如果是数值也可以做数值计算
列表：使用`{{ my_int[1] }}`、`{{ my_list.1 }}`获取对应元素
字典：使用`{{ foo.name }}`、`{{ foo.get("age") }}`、`{{ foo["gender"] }}`通过k获得v
字符串：如果字符串内容是一个html标签，并且展示是也是要展示为标签可以使用`{{ my_str|safe }}` 或者在后端中配置

~~~python

视图函数中
from flask import Markup  # 导入 flask 中的 Markup 模块
tag = "<input type='text' name='user' value='DragonFire'>"
markup_tag = Markup(tag)    #Markup帮助咱们在HTML的标签上做了一层封装,让Jinja2模板语言知道这是一个安全的HTML标签
~~~

### 方法

自定义方法，并使用

~~~python

视图函数中
def ab(a,b):
    return a+b
@app.route('/')
def index():
    return render_template("index.html",funab=ab)   #将方法对象传递
~~~

~~~html
摸板中

{{ funab(1,2) }}    #可以传递参数
~~~

自定义全局方法

~~~python

@app.template_global()  # 定义全局模板函数
def a_b_sum(a, b):
    return a + b


@app.template_filter()  # 定义全局模板函数
def a_b_c_sum(a, b, c):
    return a + b + c
~~~

~~~html

{{ a_b_c_sum(1，2，3) }}    不在需要传递方法变量
{{ 1 | a_b_c_sum(197,2) }}
~~~

## 逻辑方法

~~~html

fot循环
{% for foo in g %}

{% endfor %}
if判断
{% if g %}

{% elif g %}
    
{% else %}
    
{% endif %}
~~~

### 摸板继承

~~~html

父摸板
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Welcome OldboyEDU</h1>
    <h2>下面的内容是不一样的</h2>
    {% block content %} #钩子名称

    {% endblock %}  #结束钩子
    <h2>上面的内容是不一样的,但是下面的内容是一样的</h2>
    <h1>OldboyEDU is Good</h1>
</body>
</html>
~~~

~~~html

子摸板
{% extends "index.html" %}  #声明父摸板文件名称
{% block content %} #开启钩子，钩子名称呀和父摸板钩子名称一致
    <form>
        用户名:<input type="text" name="user">
        密码:<input type="text" name="pwd">
    </form>
{% endblock %}  #关闭钩子
~~~

~~~python

视图函数
@app.route("/login")
def login():
    return render_template("子摸板路径")
~~~

### 组件

~~~html
组件文件
<form>
    用户名:<input type="text" name="user">
    密码:<input type="text" name="pwd">
</form>
~~~

~~~html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Welcome OldboyEDU</h1>
    <h2>下面的内容是不一样的</h2>
    {% include "组件文件路径" %}
    <h2>上面的内容是不一样的,但是下面的内容是一样的</h2>
    <h1>OldboyEDU is Good</h1>
</body>
</html>
~~~

类似html中iframe标签

### 宏

~~~html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1>Welcome OldboyEDU</h1>

{% macro type_text(name,type) %}    #开启宏，并定义名称与传递的参数
    <input type="{{ type }}" name="{{ name }}" value="{{ name }}">
{% endmacro %}

<h2>在下方是使用宏来生成input标签</h2>

{{ type_text("one","text") }}   #生成 <input type="one" name="text" value="text">
{{ type_text("two","text") }}

</body>
</html>
~~~
