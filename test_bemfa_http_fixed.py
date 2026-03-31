#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试巴法云 HTTP 推送方式"""

import requests
import hashlib
import time
import json

# 巴法云配置
BAFA_UID = "camera"  # 设备名作为 UID
BAFA_KEY = "9f834521e7cb4f4b891b5f7351c9bd4a"  # 设备私钥


def test_http_push():
    """测试 HTTP 推送"""
    print("=" * 60)
    print("测试巴法云 HTTP 推送")
    print("=" * 60)

    # 巴法云 HTTP API
    url = "http://push.bemfa.com/msg/push/"

    # 消息内容
    message = {
        "cmd": "test",
        "message": "HTTP 推送测试 - 模型更新通知",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "test": True,
    }

    # 计算签名（巴法云要求）
    # sign = MD5(uid + key + msg)
    msg_str = json.dumps(message, ensure_ascii=False)
    sign_str = BAFA_UID + BAFA_KEY + msg_str
    sign = hashlib.md5(sign_str.encode()).hexdigest()

    # 请求参数
    params = {"uid": BAFA_UID, "msg": msg_str, "sign": sign}

    print(f"\nURL: {url}")
    print(f"UID: {BAFA_UID}")
    print(f"Message: {message}")
    print(f"Sign: {sign}")
    print()

    try:
        # 发送 GET 请求（巴法云使用 GET）
        response = requests.get(url, params=params, timeout=10)

        print(f"响应状态码：{response.status_code}")
        print(f"响应内容：{response.text}")

        if response.status_code == 200:
            try:
                result = response.json()
                if result.get("code") == 200:
                    print("\n[OK] HTTP 推送成功！")
                    return True
                else:
                    print(f"\n[ERROR] HTTP 推送失败：{result}")
                    return False
            except:
                print(f"\n[ERROR] 响应解析失败")
                return False
        else:
            print(f"\n[ERROR] HTTP 请求失败")
            return False

    except Exception as e:
        print(f"\n[ERROR] 测试异常：{e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    try:
        test_http_push()
    except KeyboardInterrupt:
        print("\n\n[INFO] 用户中断")
