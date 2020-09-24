# js与bom(浏览器对象模型)、dom(文档对象模型) {ignore}

---

[toc]

## BOM 浏览器对象模型

### 窗口对象和他的子对象

~~~js
navigator.appName;  #浏览器全称
navigator.platform;     #操作系统
history.forward();      #向前一页
history.back();     #向后一页
location.href;   #获取当前页面的url
location.href="url";     #跳转到指定页面
location.reload();      #刷新当前页面
~~~

### 弹出框

~~~js

alert("你看到了吗？");  #弹出只有确认的弹出框
confirm("你确定吗？");  #弹出有确认取消的选择框,并在用户操作后返回ture或false
prompt("请在下方输入",默认显示);      #弹出输入框,并在用户确认后返回输入的内容
~~~

### 计时器(异步)

~~~js

setTimeout(js字符,时间(毫秒));  #在指定时间后执行js字符串的代码
var a=setTimeout(function(){js代码},时间(毫秒));      #将要执行的js代码用函数封装起来
clearTimeout(a);    #清除计时器

var a=setInterval(function(){js代码},时间(毫秒));   #每隔指定时间执行函数
clearInterval(a)    #清除循环计时器
~~~

## DOM 文档对象模型

### 选择器

#### 直接查找

~~~js
document.getElementById("id值");    #根据id查找标签
document.getElementByClassName("class值")   #根据class值查找标签,多个值就是数值
document.getElementByTagName("标签名")  #根据标签名称查找标签,多个值就是数组
~~~

#### 间接查找

~~~js

var a=document.getElementByTagName("标签名");
a.parentElement;    #父节点标签
a.children;     #所有子标签
a.firstElementChild;    #第一个子标签
a.lastElementChild;     #最后一个子标签
a.nextElementSibling;   #下一个兄弟标签
a.previousElementSibling;   #上一个兄弟标签
~~~

### 节点操作

~~~js

创造节点
var a=document.createElement("标签名称")

添加节点
var b=document.个体RlementByTagName("div");
b.appendChild(a);    #将a标签添加到b标签的子标签的最后

b.insertBefore(a,b1);    #将a标签添加b标签的子标签b1前

删除节点
b.removeChild(d1);   #删除b标签的子标签

替换节点
b.replaceChild(a,b1);   #用a标签替换b标签的子标签b1
~~~

### 文本操作

~~~js

a.innerText;    #查看a标签的内容
a.innerHTML;    #查看a标签的内容包括标签

a.innerText="<a href=''>百度</a>";  #对a标签写入改文本
a.innerHTML="<a href=''>百度</a>";   #对a标签写入,可以识别标签
~~~

### 属性操作

~~~js

a.setAttribute("href":"www.baidu.com");  #添加属性与值
a.getAttribute("href");  #返还属性值
a.removeAttribute("href");  #删除属性与值
~~~

~~~js

对与输入标签input、select、textarea
a.value;    #返回用户输入的内容
a.value="456";  #设置值
~~~

### class操作

~~~js

a.classList;    #返回标签的所有class值
a.classList.add("np");  #添加class属性值
a.classList.remove("np");   #删除class的该属性
a.classList.contains("np");     #判断class是否有该值,有就返回true,无就返回false
a.classList.toggle("np");   #判断class是否有该值,有就删除,没有就添加
~~~

### csss操作

~~~js

a.style.backgroudColor="red";   #设置css属性,有横杠的css属性,写法要去掉横杠,并且横杠后面的单词首字母大写
~~~

## 事件

~~~js

绑定事件的两种方法

<div id="d1" class="c1" onclick="f1();"></div>
<script>
    function f1() {
        var d = document.getElementById('d1');
        this.style.backgroundColor = 'yellow';  #tihs类似python类中的self,及标签本身
    }
</script>

为了降低耦合,使用第二中绑定方式
<div id="d1" class="c1"></div>

    var d = document.getElementById('d1');
    d.onclick = function () {
        d.style.backgroundColor = 'yellow';
    }
~~~

事件|描述|
--|--|
onclick|当用户点击某个对象时调用的事件句柄|
ondblclick|当用户双击某个对象时调用的事件句柄|
onfocus|元素获得焦点(输入框)|
onblur|元素失去焦点。(用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.)|
onchange|域的内容被改变(通常用于表单元素,当元素内容被改变时触发.)|
onkeydown|某个键盘按键被按下|
onkeypress|某个键盘按键被按下并松开|
onkeyup|某个键盘按键被松开|
onload|一张页面或一幅图像完成加载|
onmousedown|鼠标按钮被按下|
onmousemove|鼠标被移动|
onmouseout|鼠标从某元素移开|
onmouseover|鼠标移到某元素之上|
onselect|在文本框中的文本被选中时发生|
onsubmit|确认按钮被点击，使用的对象是form|
