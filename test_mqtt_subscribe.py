#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""本地 MQTT 订阅测试脚本"""

import paho.mqtt.client as mqtt
import json


def on_message(client, userdata, msg):
    """消息回调"""
    print("\n" + "=" * 60)
    print("收到 MQTT 消息！")
    print("=" * 60)
    print(f"主题：{msg.topic}")
    try:
        data = json.loads(msg.payload.decode())
        print(f"内容：{json.dumps(data, indent=2, ensure_ascii=False)}")
    except:
        print(f"内容：{msg.payload.decode()}")
    print("=" * 60)


# 连接 EMQX 公共 Broker
client = mqtt.Client()
client.on_message = on_message

print("正在连接 EMQX 公共 Broker...")
client.connect("broker.emqx.io", 1883, 60)
print("已连接！")

print("正在订阅主题 camera/update...")
client.subscribe("camera/update")
print("已订阅！")

print("\n正在监听 MQTT 消息...（按 Ctrl+C 停止）")
client.loop_forever()
