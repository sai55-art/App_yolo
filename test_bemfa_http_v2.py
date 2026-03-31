#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试巴法云 HTTP 推送方式（使用正确的 API）"""

import requests
import hashlib
import time
import json
import sys

# 设置控制台编码
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# 巴法云配置
BAFA_UID = "camera"  # 设备名
BAFA_KEY = "9f834521e7cb4f4b891b5f7351c9bd4a"  # 设备私钥


def test_http_push():
    """测试 HTTP 推送"""
    print("=" * 60)
    print("测试巴法云 HTTP 推送")
    print("=" * 60)

    # 巴法云 HTTP API（正确的 URL）
    url = "http://bemfa.com/msg/push/"

    # 消息内容（JSON 字符串）
    message = {
        "cmd": "test",
        "message": "HTTP 推送测试",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    msg_str = json.dumps(message, ensure_ascii=False)

    # 计算签名
    # 巴法云签名规则：sign = MD5(uid + key + msg)
    sign_str = BAFA_UID + BAFA_KEY + msg_str
    sign = hashlib.md5(sign_str.encode()).hexdigest()

    # 请求参数（POST 表单）
    data = {"uid": BAFA_UID, "msg": msg_str, "sign": sign}

    print(f"\nURL: {url}")
    print(f"UID: {BAFA_UID}")
    print(f"KEY: {BAFA_KEY[:8]}...")
    print(f"Message: {msg_str}")
    print(f"Sign: {sign}")
    print()

    try:
        # 发送 POST 请求
        print("正在发送请求...")
        response = requests.post(url, data=data, timeout=10)

        print(f"响应状态码：{response.status_code}")
        print(f"响应内容：{response.text}")

        if response.status_code == 200:
            try:
                result = response.json()
                code = result.get("code")
                msg = result.get("msg", "")

                if code == 200:
                    print("\n[OK] HTTP 推送成功！")
                    print(f"   返回消息：{msg}")
                    return True
                else:
                    print(f"\n[ERROR] HTTP 推送失败：{code} - {msg}")
                    return False
            except Exception as e:
                print(f"\n[ERROR] 响应解析失败：{e}")
                return False
        else:
            print(f"\n[ERROR] HTTP 请求失败：{response.status_code}")
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
