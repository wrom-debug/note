# css {ignore}

---

[toc]

## css代码引入

~~~html

方式1
在head标签中写入
 <style>
     h1{color: red;}
 </style>
方式2
在标签中写入
<div style="background:rgb(255, 0, 0);width: 100px;height: 100px;">div标签</div>
方式3
外部文件引入
在head标签里写link标签
<link rel="stylesheet" href="1.css">
css文件中写style标签内的内容
~~~

## css选择器

### 基本选择器

匹配对象：

~~~html

<div id="c1" class="c2"><a>aa</a></div>
<a>456</a>
~~~

~~~css

元素选择器  #匹配指定的标签
    标签名{css属性:属性值;}
    div{background:red;}

id选择器    #匹配id值符合的标签
    #id值{css属性:属性值;}
    #c1{background:red;}

类选择器    #匹配类值符合的标签
    .class值{css属性:属性值;}
    .c2{background:red;}

通用选择器  #匹配所有标签
    *{css属性:属性值;}

~~~

### 组合选择器

**确认选择器**(匹配选择器1并符合选择器2的标签)

~~~css

选择器1选择器2{css属性:属性值;}
div#c1{background:red;}
~~~

**后代选择器**(匹配选择器1的后代中所有符合选择器2的标签)

~~~css

选择器1 选择器2{css属性:属性值;}  
div a{background:red;}
~~~

**儿子选择器**(匹配选择器1的子标签中所有符合选择器2的标签)

~~~css

选择器1>选择器2{css属性:属性值;}
div>a{background:red;}
~~~

**毗邻选择器**(匹配选择器1的下一个兄弟标签中符合选择器2的标签)

~~~css

选择器1+选择器{css属性:属性值;}
div+a{background:red;}
~~~

**弟弟标签**(匹配选择器1之前的兄弟标签中符合选择器2的标签)

~~~css

选择器1~选择器2{css属性:属性值;}
div~a{background:red;}
~~~

### 属性选择器

~~~css

通过属性名匹配
[属性名]{css属性:属性值;}
[href]{background:red;}

通过属性名与对应的值匹配
[属性名=属性值]{css属性:属性值;}
[id="c1"]{background:red;}
~~~

### 分组

~~~css

选择器1,选择器2...{css属性:属性值;}
div,a{background:red;}
~~~

### 伪类选择器

~~~css

/* a标签未访问 */
a:link{color:red;}

/* a标签已访问 */
a:visited{color:green;}

/* 鼠标移动的某标签上 */
a:hover{color:green;}

/* 点下某标签 */
a:active{color:red}

/* input标签输入框取得焦点 */
input:focus{background-color:pink;}
~~~

### 伪元素选择器

~~~css

/* 文本第一个字符 */
a:first-letter{color: red;}

/* 标签内容前插入内容 */
a:before{content:"文本前加的内容"}

/* 标签内容后插入内容 */
a:after{content:"文本后加的内容"}
~~~

### 选择器的优先级

选择器|优先及
--|---:|
id选择器|100|
继承|0|
类选择器|10|
元素选择器|1|
在标签中填写|10000|
在属性值后跟！important|最大

(**优先级不会进位**)

## CSS属性

~~~css

width: 100px;   #宽度
height: 100px;  #高度
background-color:red ;  #背景颜色

~~~

宽度高度设置只有块级标签才可以设置，内敛标签的高度和宽度由内容决定
a标签内的css样式要定位到a标签上才生效

### 字体属性

~~~css

font-family: '楷体';    #字体（属性值可以写对应字体）
color: black;   #字体颜色
font-sizepx:14px;   #字体大小（默认为16px）
font-weight: bold;   #字体粗细
~~~

字体粗细值|描述|
--|--|
normal|默认，标准|
bold|粗体|
bloder|更粗|
lighter|更细|
100~900|由细到粗，400=默认|

~~~css

text-align: right;  #字体对齐
~~~

值|说明|
--|--|
left|左对齐 默认|
right|右对齐|
center|居中|

~~~css

text-decoration:none;   #下划线
~~~

值|描述|
--|--|
none|取消|
underline|下划线|
overline|上划线|
line-through|删除线|

~~~css

text-indent: 32px;  #首行缩进，一个字大小默认16px
~~~

### 背景颜色

~~~css

background：red url('图片路径') no-repeat right top
颜色 图片路径 是否平铺 图片位置
~~~

- 颜色的四种写法:
  - 直接写颜色名称：red、black
  - rgb：rgb(255,255,255)
  - 16进制：#ff2525
    - 可以简写位#f2525两位相同可以缩写
  - rgba:rgba(255,255,255,0.5)
    - 最后一位为透明度

平铺值|描述|
--|--|
no-repeat|不平铺|
reperat|平铺 默认|

图片位置两种写法：

1. 具体位置：10px 20px / 距右边距离 距上面距离
2. 方位描述: top center bottom /上 中 下
left center right / 左 中 右

### 边框样式

~~~css

border-width: 10px;
border-style: dotted;
border-color: red;
简写:
border: 宽度 样式 颜色;
border: 2px dotted red;
~~~

样式值|描述|
--|--|
none|无边框|
dotted|点状虚边框|
dashed|矩形虚边框|
solid|实线边框|

还可单独设置某一边边框，例如：

~~~css

dorder-top-color: black;
dorder-left-style：none;
dorder-top: 2px dotted red;
~~~

~~~css

border-radius: 50%;
~~~
