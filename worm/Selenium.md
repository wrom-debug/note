# selenium-浏览器自动化

---
[toc]

## 环境准备

### 安装selenium

~~~shell

pip install selenium
pip3 install selenium
~~~

根据安装的pip版本来安装

### 浏览器驱动

安装对应浏览器的对应版本驱动，下载地址如下

谷歌浏览器chrome：<http://npm.taobao.org/mirrors/chromedriver/>

火狐浏览器firefox：<http://npm.taobao.org/mirrors/geckodriver/>

当然也有使用其他的浏览器，自行百度

## 使用

### 声明浏览器

~~~python

import selenium import webdriver
chrome=webdriver.Chrome(r'firefox驱动路径')
firefox=webdriver.Firefox(r'firefox驱动路径')
edge=webdriver.Edge()
phantomjs=wedbriver.Phantomjs()
webdriver.ChromeOptions
webdriver.Ie
webdriver.Opera
webdriver.Remote
webdriver.DesiredCapabilities
webdriver.ActionChains
webdriver.TouchActions
webdriver.Proxy
~~~

### 访问

~~~python

chrome.get(url)
~~~

- back():返回
- forward():前进

### 查找节点

#### 查找一个节点

可以通过id值查找、xpath查找、标签名称查找、css查找

~~~python

chrome.find_elemt_by_id('标签id值')
chrome.find_elemt_by_name('标签名称')
chrome.find_elemt_by_xpath('xpath表达式')
chrome.find_elemt_by_css_selector('css选择器')
~~~

所有的查找方法：

- find_elemt_by_id
- find_elemt_by_name
- find_elemt_by_xpath
- find_elemt_by_link_text
- find_elemt_by_partial_link_text
- find_elemt_by_tag_name
- find_elemt_by_class_name
- find_elemt_by_css_selector

返回节点的webelement对象

#### 查找多个节点

和查找一个节点一样只是`find_elemt`改写成`ind_elemts`

返回的是一个匹配的节点列表

### 节点交互

~~~python

inp=chrome.find_elemt_by_xpath('xpath表达式')
inp.send_key('需要输入的文本')  #输入文本
inp.clear() #清空文字
inp.click() #点击
~~~

### 动作链

对于不针对摸一个节点的交互指令，例如按下某个按键，拖拽等使用

~~~python

from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
action = ActionChains(bro)
action.click_and_hold(div_tag)
action.move_by_offset(17,5).perform()   #preform让动作链立即执行
action.release()    #关闭动作链
~~~

- click():点击
- click_and_hold():点击不放
- context_click():上下文点击
- double_click():双击
- drag_and_drop(起始标签,目标标签):拖动起始标签到目标标签位置
- drag_and_drop_offset(起始标签，x距离，y距离):拖动起始标签移动xy距离
- key_down('按键值'):按下一个按键不释放
- key_up('按键值'):释放一个按键
- move_by_offste(x，y):移动想xy距离
- move_to_element(标签):移动到标签的中间
- move_to_element_with_offset(标签，x，y):移动到元素左上角并移动xy距离
- release():释放点击
- send_key('文本'):输入文本内容
- send_key_to_element(标签,'文本'):将文本发送给标签

### 执行js

~~~python

chrome.execute_script('js代码') #执行js代码
chrome.execute_async_script('js代码')   #异步执行js代码
~~~

### 获取节点数据

- get_attribute('属性'):获取节点属性
- get_text():获取节点文本
- id:获取节点id值
- location:获取节点位置
- tag_naem:获取节点标签名称
- size:获取节点大小

### 切换iframe

~~~python

chrome.switch_to.frame('iframe标签id')  #进入子页面，iframe标签
chrome.switch_to.parent_frame() #返回父页面
~~~

### 延时等待

由于网页会有部分数据是使用ajax加载所有需要等待加载完成

#### 隐式等待

设置的是全局等待

~~~python

br.implicitly_wait(10)  #在定位标签前添加这个，定位节点时如果一开始没有定位到，一直等待节点出现或者超时报错。
~~~

#### 显式等待

~~~python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))    
element.send_keys('selenium')
~~~

WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

driver：浏览器驱动
timeout：最长超时时间，默认以秒为单位
poll_frequency：检测的间隔（步长）时间，默认为0.5S
ignored_exceptions：超时后的异常信息，默认情况下抛NoSuchElementException异常

WebDriverWait再调用until方法，并传入expected_conditions类的条件
|条件|说明|
|--|--|
|itle_is|判断当前页面的 title 是否完全等于（==）预期字符串，返回布尔值|
|title_contains|判断当前页面的 title 是否包含预期字符串，返回布尔值|
|presence_of_element_located|判断某个元素是否被加到了 dom 树里，并不代表该元素一定可见|
|visibility_of_element_located|断元素是否可见（可见代表元素非隐藏，并且元素宽和高都不等于 0）|
|visibility_of|同上一方法，只是上一方法参数为locator，这个方法参数是 定位后的元素|
|presence_of_all_elements_located|判断是否至少有 1 个元素存在于 dom 树中|
|text_to_be_present_in_element|判断某个元素中的 text 是否 包含 了预期的字符串|
|text_to_be_present_in_element_value|判断某个元素中的 value 属性是否包含 了预期的字符串|
|frame_to_be_available_and_switch_to_it|判断该 frame 是否可以 switch进去，如果可以的话，返回 True 并且 switch 进去，否则返回 False|
|invisibility_of_element_located|判断某个元素中是否不存在于dom树或不可见|
|element_to_be_clickable|判断某个元素中是否可见并且可点击|
|staleness_of|等某个元素从 dom 树中移除，注意，这个方法也是返回 True或 False|
|element_to_be_selected|判断某个元素是否被选中了,一般用在下拉列表|
|element_selection_state_to_be|判断某个元素的选中状态是否符合预期|
|element_located_selection_state_to_be|跟上面的方法作用一样，只是上面的方法传入定位到的 element，而这个方法传入 locator|
|alert_is_present|判断页面上是否存在 alert|

### cookies

~~~python

chrome.get_cookies()    #获取cookie
chrome.add_cookie(cookie字典)   #添加cookie+6
chrome.delete_all_cookies() #删除所有cookies
~~~

### 选项卡

~~~python

chrome.execute_script('window.open()') #多开一个选项卡
window_list=chrome.window_handles   #获取选项卡代号
chrome.switch_to_window(window_list[1]) #切换到第二个选项卡
~~~

### 异常处理

~~~python

from selenium.common.exceptions import TimeoutException,NoSuchElementException

try：
    chrome.get("http://wwww.baidu.com")
except TimeoutException:
    print("超时")
try:
    chrome.frin_lement_by_id("hello")
except NoSuchElementException:
    print("没有找到")
finally:
    chrome.close()
~~~

### chrome无头浏览器

~~~python

#使用谷歌无头浏览器
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(r'chromedriver.exe',chrome_options=chrome_options)
driver.get('https://www.cnblogs.com/')
print(driver.page_source)
~~~

### 免疫js判断selenium

~~~python

#如何规避selenium被检测
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(r'chromedriver.exe',options=option)
driver.get('https://www.taobao.com/')
~~~
