#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试巴法云 MQTT 连接"""

import paho.mqtt.client as mqtt
import time

# 巴法云配置
BROKER = "bemfa.com"
PORT = 9501  # 尝试 WebSocket 端口
USERNAME = "18439120467"
PASSWORD = "ms828160"
TOPIC = "camera/update"


def test_connection():
    """测试 MQTT 连接"""
    print("=" * 60)
    print("测试巴法云 MQTT 连接")
    print("=" * 60)
    print(f"\nBroker: {BROKER}:{PORT}")
    print(f"Username: {USERNAME}")
    print(f"Topic: {TOPIC}")
    print()

    connected = False

    def on_connect(client, userdata, flags, rc):
        nonlocal connected
        if rc == 0:
            connected = True
            print("[OK] MQTT 连接成功！")
        else:
            print(f"[ERROR] MQTT 连接失败：错误码 {rc}")
            error_msgs = {
                1: "协议版本错误",
                2: "客户端 ID 无效",
                3: "服务器不可用",
                4: "用户名/密码错误",
                5: "未授权",
            }
            print(f"   说明：{error_msgs.get(rc, '未知错误')}")

    def on_disconnect(client, userdata, rc):
        print(f"[INFO] 已断开连接：{rc}")

    try:
        # 创建客户端 - 巴法云要求 Client ID 包含用户名
        client_id = f"{USERNAME}@{int(time.time())}"
        print(f"Client ID: {client_id}")
        client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv311)

        # 设置回调
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect

        # 巴法云认证：尝试不同的组合
        # 方式 1: 使用私钥
        PRIVATE_KEY = "f834521e7cb4f4b891b5f7351c9bd4a"

        # 尝试使用手机号 + 私钥
        print(f"尝试认证：{USERNAME} + {PRIVATE_KEY[:8]}...")
        client.username_pw_set(USERNAME, PRIVATE_KEY)

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
                "cmd": "test",
                "message": "MQTT 连接测试",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }

            result = client.publish(TOPIC, str(test_msg), qos=1)

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
            return True
        else:
            print("\n[ERROR] 连接超时")
            return False

    except Exception as e:
        print(f"\n[ERROR] 测试异常：{e}")
        return False


if __name__ == "__main__":
    try:
        test_connection()
    except KeyboardInterrupt:
        print("\n\n[INFO] 用户中断")
