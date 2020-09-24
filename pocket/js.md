# JavaScript {ignore}

---

[toc]

## js导入

~~~html

方式1：
<scrip>js代码</scrip>
方式2：
<scrip src="js文件路径"></scrip>
~~~

## 声明变量

~~~js

var a;      #声明变量时如果不赋值时变量的值就为undefined
~~~

## 基本数据类型

### 数值类型 Number

~~~js

var a=10;
var b=1.01;
var c=123e5;
以上变量均是数值类型
typeof a;       #可以查看数据类型
~~~

### 字符类型 String

~~~js

var a="hello";
var b="wrod";
var c=a+b;
字符允许相加
console.log(c);     #可以打印内容
~~~

### 类型转换

~~~js

var a=parseInt("123.5")       #返回整数123
var a=parseFloat("123.5")       #返回浮点数123.5
如果转化的对象不可以转换成数值类型,则会返回NaN,一个特殊的数值,表示不是数值.
~~~

### 字符串常用方法

~~~js

1.参看长度
var a="asd";
a.length;       #3

2.移除空白
var a=" 123 ";
a.trim();       #"123"
a.trimLeft();   #去左空白
a.trimRight();  #去右边空白

3.索引找字符
var a="asd";
a.charAt(2);    #js中索引从1开始

4.字符拼接
var a="123";
var b="456";
a.concat(b);    #"123456"

5.字符找索引
var a="asd";
a.indexOf("a");     #2

6.切片
var a="helloword";
a.slice(5,6);    #"w"

7.大小写变换
var a="HelloWord";
a.toUpperCase();    #"HELLOWORD"
a.toLowerCase();    #"helloword"

8.拆分
var a="HelloWord";
a.split('e');   #["H","llWord"]
a.split('e',1);     #["H"]
~~~

### 布尔值

~~~js

var a=ture;
var b=false;
""、0、null、undefined、NaN，均代表false。
~~~

### 空值

~~~js

var a=null;     #值为空,与ubdefined的没有给值的空不同
~~~

### 对象

~~~js

var a=new String("asd")
~~~

## 较复杂的对象

### 数组

~~~js

var a=[11,22,33];
typeof a;   #object
~~~

### 数组常用方法

~~~js

1.索引取值
var a=[1,2,3,4];
console.log(a[1]);      #2
数组的索引是从0开始的,不支持负数

2.长度
var a=[1,2,3,4];
a.length;       #4

3.尾部添加与删除
var a=[1,2,3];
a.push("a");    #[1,2,3,"a"]
a.pop();    #"a"

4.头部添加与删除
var a=[1,2,3];
a.unshift("a");     #["a",1,2,3]
a.shift();      #"a"

5.排序
var a=[11,21,100];
a.stor();   #[100,11,21]
stor会依据每个值的第一位的ascll码大小依次排序
function sortNumber(a,b){return a - b;}
a.stor(sortNumber);     #[11,21,100]

6.删除
var a=[1,2,3,4];
a.splice(1,2,"a","b");      #[2,3]
a;      #[1,'a','b',4]
.splice(起始位置,删除长度,替换元素)
~~~

### 自定义对象

~~~js

var a={"name":"alex",age:"18"}  #类似python的字典,但是键可以不用引号
~~~

### date 时间对象

~~~js

var a=new Date();   #获取当前时间
a.toLocaleString()  #当前时间字符串
var a=new Date("2020/6/6 11:11")        #赋值给定的时间
~~~

### date对象方法

~~~js

ar d = new Date();
getDate()                 获取日
getDay ()                 获取星期 ，数字表示（0-6），周日数字是0
getMonth ()               获取月（0-11,0表示1月,依次类推）
getFullYear ()            获取完整年份
getHours ()               获取小时
getMinutes ()             获取分钟
getSeconds ()             获取秒
getMilliseconds ()        获取毫秒
getTime ()                返回累计毫秒数(从1970/1/1午夜),时间戳
~~~

### json对象

~~~js

JSON字符串转换成对象  反序列化
var obj = JSON.parse(str1);
对象转换成JSON字符串  序列化
var str = JSON.stringify(obj1);
~~~

### RegExp正则对象

~~~js

var reg1 = new RegExp(正则表达式);

简写
var reg2 = /^[a-zA-Z][a-zA-Z0-9_]{5,11}$/;      #匹配字母开头后面是字母或数字的6-12位字符串

简写后加上g代表全部匹配,i代表不区分大小写

匹配
reg1.test(str);  #符合返回true,不符合返回fales

注意如果
reg1.test()那么就等于reg1.test("undefined")
~~~

### 正则的其他方法

~~~js
str.match(re);   #返回匹配字符
str.search(re);  #返回匹配字符的索引,只返回第一个匹配的字符
str.spli(re);    #依据匹配的字符对原字符串进行切割
str.replace(re,str);   #对匹配的字符进行替换
~~~

## 运算符

### 算数运算符

~~~js

+ - * / % -- ++
加 减 乘 除 整除 自减 自增
~~~

### 比较运算符

~~~js

> >= < <= != == !== ===
js中是区分强等于与若等于的,强等于会判断数据类型.
~~~

### 逻辑运算符

~~~js

&& || !
与 或 非
~~~

### 赋值运算符

~~~js

= += -= *= /=
等于 加等 减等 乘等 除等
~~~

### 流程控制

~~~js

判断控制
if-else if-else
switch(a){
case 1:
a值为1时运行的代码;
break;
case 2:
a值为2时运行的代码;
break;
default:
均不符合以上条件时执行的代码;
}

循环控制
for(var a=0;a<10;a++){循环执行语句}
for(a in b){循环执行语句}
while(i<10){循环执行语句}
~~~

### 三元运算符

~~~js

var c=1>2?1:2       #问号前的的判断语句,如果真,那么就赋值冒号前的值,如果假,那么就赋值莫号后的值
~~~

## 函数

~~~js

一般函数
function my(a,b){函数代码;return 值}

匿名函数
var c=function(a,b){函数代码}
c(a,b)      #执行匿名函数

立即执行函数
(function(a,b){函数代码})
~~~

### 变量作用域

全局变量:
    在函数外声明的变量
    从变量被声明开始到页面结束后被删除
局部变量:
    函数内部声明的变量
    从变量被声明开始到函数运行结束后删除
变量作用域
    首先在本函数内部查找局部变量,找不到就在外层函数中查找,逐步到最外层的全局变量.

闭包就是函数内部定义函数,并且调用改内部函数

## 面向对象

~~~js

定义结构体
function class(name){this.name=name}

给结构体绑定方法
class.prototype.add=function(a,b){方法代码}
~~~

## math计算模块

~~~js

Math.abs(x)      返回数的绝对值。
exp(x)      返回 e 的指数。
floor(x)    小数部分进行直接舍去。
log(x)      返回数的自然对数（底为e）。
max(x,y)    返回 x 和 y 中的最高值。
min(x,y)    返回 x 和 y 中的最低值。
pow(x,y)    返回 x 的 y 次幂。
random()    返回 0 ~ 1 之间的随机数。
round(x)    把数四舍五入为最接近的整数。
sin(x)      返回数的正弦。
sqrt(x)     返回数的平方根。
tan(x)      返回角的正切。
~~~
