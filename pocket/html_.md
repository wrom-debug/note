#  html
  
  
---
  
- [html](#html)
  - [标签的分类](#标签的分类)
  - [head标签中的标签](#head标签中的标签)
  - [body标签中的标签](#body标签中的标签)
    - [特殊字符](#特殊字符)
    - [基本标签](#基本标签)
    - [img-图片标签](#img-图片标签)
    - [a-超链接标签](#a-超链接标签)
    - [ul、li\ol、li-列表标签](#ulliolli-列表标签)
    - [dl-标题列表标签](#dl-标题列表标签)
    - [div、span-容器标签](#divspan-容器标签)
    - [table-表格标签](#table-表格标签)
    - [from-表单标签](#from-表单标签)
      - [input-输入标签](#input-输入标签)
        - [label标签](#label标签)
      - [select-下拉选择框标签](#select-下拉选择框标签)
      - [textarea-多行文本标签](#textarea-多行文本标签)
    - [iframe-框架标签](#iframe-框架标签)
  
##  标签的分类
  
  
按标签样式分类：两类
  
1. 内敛标签（行内标签）：不独占一行，内敛标签只能嵌套内敛标签
b\i\u\button\span\img\a
  
2. 块级标签（行外标签）：自己独占一行，可以嵌套内敛标签和某些块级标签
\h1-h6\br\hr\p\div
  
##  head标签中的标签
  
  
~~~html
  
<title>网页标题</title>
<meta/>定义网页源信息\配置信息
~~~
  
##  body标签中的标签
  
  
###  特殊字符
  
  
~~~html
  
空格:&nbsp;
小于号:&lt;
大于号:&gt;
&符号:&amp;
...
~~~
  
###  基本标签
  
  
~~~html
  
字体标签：
    <b>加粗</b>
    <i>斜体</i>
    <u>下划线</u>
    <s>删除</s>
~~~
  
![字体样式](/img/142226.png "字体样式")
  
~~~html
  
段落标签：
    <p>段落标签</p>
    //每段之间会有行间隔
~~~
  
![段落样式](/img/142445.png "段落样式")
  
~~~html
  
标题标签：
    <h1>标题1</h1>
    <h2>标题2</h2>
    <h3>标题3</h3>
    <h4>标题4</h4>
    <h5>标题5</h5>
    <h6>标题6</h6>
~~~
  
![标题样式](/img/142709.png "标题样式")
  
~~~html
  
换行：
    <br>
~~~
  
![换行样式](/img/142807.png "换行样式")
  
~~~html
  
分割线：
    <hr>
~~~
  
![分割线样式](/img/142936.png "分割线样式")
  
###  img-图片标签
  
  
~~~html
  
<img src="/笔记/img/1.jpg" alt="憨憨" title="憨憨" width="100px" height="100px">
~~~
  
![图片样式](/img/144551.png "图片样式")
  
src属性：图片路径，可以为相对路径、绝对路径、网络路径
alt属性：图片加载失败后显示的字符
title属性：鼠标放置在图片上显示的提示（基本所有标签均可以设置该属性，均为该效果）
width、height属性：图片显示的大小
  
###  a-超链接标签
  
  
~~~html
  
<a href="/笔记/img/1.jpg" target="_self">图片</a>
~~~
  
![超链接样式](/img/144702.png "超链接样式")
  
href属性：超链接路径可以为相对路径、绝对路径、网络路径
target属性：是否新建窗口
target="_self"：在当前窗口打开
target="_blank"：在新建窗口打开
  
a标签除了可以用来链接别的链接还可以用来触发锚点
  
~~~html
  
<a href="#对应位置标签的class值/对应位置a标签的name属性值" target="_self">锚点</a>
~~~
  
###  ul、li\ol、li-列表标签
  
  
~~~html
  
<ul type="none">
    <li>周一</li>
    <li>周二</li>
</ul>
或
<ol type="none">
    <li>周一</li>
    <li>周二</li>
</ol>
~~~
  
![列表样式](/img/145202.png "列表样式")
  
ul标签为无序列表
type属性:列表前的样式
  
值|备注|
---|---
disc(默认)|实心圆
circle|空心圆
square|小方块
  
ol标签为有序列表
  
值|备注|
---|---
1(默认)|数字表示(123)
A|大写字母表示(ABC)
a|小写字母表示(abc)
I|大写罗马字母表示(I II)
i|小写罗马字母表示(i ii)
  
###  dl-标题列表标签
  
  
~~~html
  
<dl>
    <dt>标题1</dt>
    <dd>标题说明</dd>
    <dt>标题2</dt>
    <dd>标题2说明</dd>
</dl>
~~~
  
![标题列表样式](/img/151131.png "标题列表样式")
  
###  div、span-容器标签
  
  
~~~html
  
<div style="background:rgb(255, 0, 0);width: 100px;height: 100px;"></div>
  
<span>span标签</span>
~~~
  
![容器样式](/img/151955.png "容器样式")
  
div标签一般用来将网页分割成不同的独立部分
span标签一般用来作为文字容器使用
  
###  table-表格标签
  
  
~~~html
  
<table border="1" cellpadding="10px" cellspacing="">
    <caption >表格标题</caption>
    <tr>
        <th>表头1</th>
        <th>表头2</th>
    </tr>
    <tr>
        <td>第一行第一列</td>
        <td>第一行第二列</td>
    </tr>
    <tr>
        <td>第二行第一列</td>
        <td>第二行第二列</td>
    </tr>
</table>
~~~
  
![表格样式](/img/154646.png "表格样式")
  
table标签
border属性：边框宽度
cellpadding属性：文字与内边框的距离
cellspacing属性：内边框与外边框
bgcolor属性：背景颜色
  
th标签
rowspan属性：向下合并单元格
colspan属性：向右合并单元格
  
###  from-表单标签
  
  
~~~html
  
  <from name="" method="" action="" ></from>
~~~
  
- name属性：表单名称
- method属性：提交方式（get安全性交低、post安全性较高）
- action属性：发送的地址，必须是有效的url
  
####  input-输入标签
  
  
~~~html
  
<input type="text" name="123" value="456" size="5" maxlength="5">
<input type="password"><br>
<input type="radio" value="1" name="456" checked>
<input type="radio" value="2" name="456">
<input type="checkbox" value="a" name="789">
<input type="checkbox" value="b"name="789">
<input type="reset" value="">
<input type="submit" value="">
<input type="file" name="" id="">
<input type="date" name="" id="">
~~~
  
![输入样式](/img/162617.png "输入样式")
  
- type属性：控件类型
  - text：文本输入
  - passwrod：密码输入，输入内容不可见
  - radio：单选
  - checkbox：多选
  - number：只能输入数字
  - date：时间输入
  - file：文件输入
  - submit：提交表单
  - reset：重置输入
  - hidden：隐藏输入框
- name属性：控件分组名称名称
- value属性：文字字段默认值/单选多选中为选中传递的值
- size属性：控件长度
- maxlengyh属性：最长字符数
- checked属性：默认选中
- readonly属性：只读，不可写入
- disabled属性：不允许操作
  
#####  label标签
  
  
~~~html
<label for="username">用户名</label>
<input id="username" type="text" name="username" value="dazhuang">
或
<label>
密码:<input type="password" name="password" value="111" disabled>
</label>
~~~
  
点击lable标签的文本也会选中绑定的input标签
  
####  select-下拉选择框标签
  
  
~~~html
  
<select name="city" size=""  multiple>
    <option value="1">北京</option>
    <option value="2">上海</option>
</select>
~~~
  
![下拉样式](/img/170058.png "下拉样式")
  
multiple属性：多选
size属性：一次显示多少内容
  
####  textarea-多行文本标签
  
  
~~~html
  
<textarea name="" id="" cols="30" rows="10">默认内容</textarea>
~~~
  
![多行文本样式](/img/170218.png "多行文本样式")
  
name属性：名称
rows属性：高度
cols属性：长度
disabled：禁用
  
###  iframe-框架标签
  
  
~~~html
  
<iframe src="" width="400" height="400" frameborder="0"></iframe>
~~~
  
![框架样式](/img/171531.png "框架样式")
  
src属性：显示的页面
width属性：宽度
height：高度
frameborder属性：边框宽度
  
使用iframe来显示目标链接页面
  
~~~html
<a href="https://www.lanqiao.cn/" target="shiyanlou">实验楼</a>
<iframe width="400" height="400" name="shiyanlou"></iframe>
~~~
  
a标签的target属性是iframe标签的name属性值，会在a标签点击后iframe中显示a标签链接的页面
  