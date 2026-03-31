#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试 EMQX 公共 MQTT Broker（用于开发测试）"""

import paho.mqtt.client as mqtt
import time
import json

# EMQX 公共 Broker 配置（无需认证）
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "camera/update"
CLIENT_ID = f"apple_yolo_{int(time.time())}"
USERNAME = ""
PASSWORD = ""

connected = False


def on_connect(client, userdata, flags, rc):
    """连接回调"""
    global connected
    if rc == 0:
        connected = True
        print("[OK] MQTT 连接成功！")
        print(f"   Broker: {BROKER}:{PORT}")
        print(f"   Topic: {TOPIC}")
    else:
        print(f"[ERROR] MQTT 连接失败：错误码 {rc}")


def on_disconnect(client, userdata, rc):
    """断开回调"""
    print(f"[INFO] 已断开连接：{rc}")


def test_connection():
    """测试 MQTT 连接"""
    print("=" * 60)
    print("测试 EMQX 公共 MQTT Broker")
    print("=" * 60)
    print()
    print(f"Broker: {BROKER}:{PORT}")
    print(f"Topic: {TOPIC}")
    print(f"Client ID: {CLIENT_ID}")
    print(f"认证：无需")
    print()

    try:
        # 创建客户端
        client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)

        # 设置回调
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect

        # 连接
        print("正在连接...")
        client.connect(BROKER, PORT, 60)

        # 启动网络循环
        client.loop_start()

        # 等待连接结果
        timeout = 10
        while not connected and timeout > 0:
            time.sleep(0.5)
            timeout -= 0.5

        if connected:
            # 发布测试消息
            print("\n正在发布测试消息...")
            test_msg = {
                "cmd": "update",
                "url": "http://test.com/model.pt",
                "md5": "abc123def456",
                "version": "test_001",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "size": 41943040,
                "test": True,
            }

            result = client.publish(
                TOPIC, json.dumps(test_msg, ensure_ascii=False), qos=1
            )

            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print("[OK] 消息发布成功！")
                print(f"   主题：{TOPIC}")
                print(f"   消息：{test_msg}")
            else:
                print(f"[ERROR] 消息发布失败：{result.rc}")

            # 等待一下
            time.sleep(1)

            # 断开
            client.disconnect()
            client.loop_stop()

            print("\n[OK] 测试完成！")
            print("\n下一步：")
            print("1. 使用 Docker 订阅主题验证消息接收")
            print("   docker run -it --rm eclipse-mosquitto mosquitto_sub \\")
            print("     -h broker.emqx.io -p 1883 \\")
            print("     -t 'camera/update' -v")
            print("\n2. 或使用网页版 MQTTX 测试")
            print("   https://mqttx.app/zh")
            return True
        else:
            print("\n[ERROR] 连接超时")
            return False

    except Exception as e:
        print(f"\n[ERROR] 测试异常：{e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    try:
        test_connection()
    except KeyboardInterrupt:
        print("\n\n[INFO] 用户中断")
