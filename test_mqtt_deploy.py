#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MQTT 传出功能测试脚本
使用方法：
1. 启动后端服务
2. 运行此脚本
"""

import sys
import json
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from backend.services.deploy_manager import DeployManager


def test_mqtt_connection():
    """测试 MQTT 连接"""
    print("=" * 60)
    print("📡 测试 MQTT 连接")
    print("=" * 60)

    manager = DeployManager()
    result = manager.test_mqtt_connection()

    if result["success"]:
        print(f"✅ {result['message']}")
        print(f"   Broker: {result.get('broker')}")
        print(f"   Topic: {result.get('topic')}")
    else:
        print(f"❌ {result['message']}")

    return result


def test_publish_model(train_id: str):
    """测试模型传出"""
    print("\n" + "=" * 60)
    print(f"📦 测试模型传出：{train_id}")
    print("=" * 60)

    manager = DeployManager()
    result = manager.publish_model(train_id)

    if result["success"]:
        print(f"✅ 传出成功！")
        print(f"   MD5: {result['data']['md5']}")
        print(f"   URL: {result['data']['download_url']}")
        print(f"   大小：{result['data']['file_size']} 字节")
        print(f"   时间：{result['data']['published_at']}")
    else:
        print(f"❌ 传出失败：{result['message']}")

    return result


def test_get_history():
    """查询传出历史"""
    print("\n" + "=" * 60)
    print("📋 查询传出历史")
    print("=" * 60)

    manager = DeployManager()
    history = manager.get_deploy_history()

    if history:
        print(f"✅ 共 {len(history)} 条传出记录")
        for i, record in enumerate(history, 1):
            print(f"\n   [{i}] 训练 ID: {record['train_id']}")
            print(f"       MD5: {record['md5']}")
            print(f"       URL: {record['download_url']}")
            print(f"       时间：{record['published_at']}")
    else:
        print("⚠️ 暂无传出记录")

    return history


def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("🚀 MQTT 模型分发功能测试")
    print("=" * 60)

    # 测试 MQTT 连接
    test_mqtt_connection()

    # 测试模型传出（使用最新的训练任务）
    print("\n💡 提示：请确保已训练完成一个模型")
    train_id = input("请输入训练任务 ID（直接回车使用 t_20260308_0812_bcca）: ").strip()
    if not train_id:
        train_id = "t_20260308_0812_bcca"

    test_publish_model(train_id)

    # 查询传出历史
    test_get_history()

    print("\n" + "=" * 60)
    print("✅ 测试完成！")
    print("=" * 60)

    # 提示下一步操作
    print("\n📌 下一步操作：")
    print("1. 打开浏览器访问：http://localhost:8000/docs")
    print("2. 查看 API 文档并测试其他接口")
    print("3. 使用 Docker 订阅 MQTT 消息：")
    print("   docker run -it --rm eclipse-mosquitto mosquitto_sub \\")
    print("     -h bemfa.com -p 1883 \\")
    print('     -u "18439120467" -P "ms828160" \\')
    print('     -t "camera/update" -v')
    print("\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断")
    except Exception as e:
        print(f"\n❌ 测试失败：{e}")
        import traceback

        traceback.print_exc()
