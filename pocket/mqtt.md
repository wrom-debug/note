# MQTT {ignore}

[toc]

## 安装并配置

### mosquitto安装

~~~shell

sudo apt-get install mosquitto mosquitto-clients
~~~

安装MQTT服务器与客户端

### 配置

~~~shell

~~~

### 测试

~~~shell

mosquitto_sub -t 'test' -d #订阅主题'test'

mosquitto_pub -d -t 'test' -m 'hello，word' #发布主题为'test'消息为'hello，word'
~~~

参数|备注|
--|--|
-d|调试模式显示更多信息
-h|服务器ip
-t|指定主题
-u|用户名
-p|密码
-i|客户端id，唯一
-m|发布的消息内容

## python

~~~shell

sudo pip install paho-mqtt
~~~

安装python-MQTT库

~~~python

import paho.mqtt.client as mqtt     #导入库
MQTTHOST = "mqtt.p2hp.com"
MQTTPORT = 1883
mqttClient = mqtt.Client()

def on_mqtt_connect():      #连接MQTT服务器
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)  #设置连接参数：ip、端口、通信最大时间（秒）
    mqttClient.loop_start()     #开启线程

def on_publish(topic, payload, qos):        # publish 消息
    mqttClient.publish(topic, payload, qos) #发布主题、消息、等级

def on_message_come(lient, userdata, msg):      # 消息处理函数
    print(msg.topic + " " + ":" + str(msg.payload))     #打印收到主题与消息

def on_subscribe():     # subscribe 消息
    mqttClient.subscribe("/server", 1)      #订阅server主题 等级
    mqttClient.on_message = on_message_come # 消息到来处理函数

def main():
    on_mqtt_connect()
    on_publish("/test/server", "Hello Python!", 1)
    on_subscribe()
    while True:
        pass

if __name__ == '__main__':
    main()
~~~
