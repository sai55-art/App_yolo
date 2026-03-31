"""
测试标注功能改进

改进内容：
1. 详细的日志记录
2. 重试机制（最多 3 次）
3. 超时时间增加到 120 秒
4. 错误统计和分类
"""

import requests
import json

# 测试配置
BASE_URL = "http://localhost:8000"
API_BASE = f"{BASE_URL}/api/v1"


def test_single_annotation():
    """测试单张图片标注"""
    print("=" * 60)
    print("测试单张图片标注")
    print("=" * 60)

    # 1. 获取图片列表
    response = requests.get(f"{API_BASE}/upload/list?limit=1")
    result = response.json()

    if not result["images"]:
        print("❌ 没有可用的图片")
        return

    image_id = result["images"][0]["image_id"]
    print(f"✅ 选择图片: {image_id}")

    # 2. 发起标注请求
    print("\n开始标注...")
    response = requests.post(
        f"{API_BASE}/annotate/",
        json={"image_ids": [image_id]},
        timeout=180,  # 3 分钟超时
    )

    result = response.json()
    print(f"\n响应状态码: {response.status_code}")
    print(f"消息: {result.get('message')}")

    if result.get("success"):
        annotation_result = result["results"][0]
        print(f"\n标注结果:")
        print(f"  成功: {annotation_result['success']}")
        print(f"  消息: {annotation_result['message']}")
        print(f"  对象数: {annotation_result['objects_count']}")

        if annotation_result["success"]:
            print(f"  标注文件: {annotation_result.get('annotation_file')}")
    else:
        print(f"❌ 标注失败")


def test_batch_annotation(batch_size=10):
    """测试批量标注"""
    print("\n" + "=" * 60)
    print(f"测试批量标注（{batch_size} 张图片）")
    print("=" * 60)

    # 1. 获取图片列表
    response = requests.get(f"{API_BASE}/upload/list?limit={batch_size}")
    result = response.json()

    if not result["images"]:
        print("❌ 没有可用的图片")
        return

    image_ids = [img["image_id"] for img in result["images"]]
    print(f"✅ 选择 {len(image_ids)} 张图片")

    # 2. 获取已标注列表
    response = requests.get(f"{API_BASE}/annotate/list")
    annotated_ids = set(
        ann["image_id"] for ann in response.json().get("annotations", [])
    )

    # 3. 过滤已标注的图片
    unannotated_ids = [iid for iid in image_ids if iid not in annotated_ids]
    print(f"✅ 未标注图片: {len(unannotated_ids)} 张")

    if not unannotated_ids:
        print("所有图片都已标注")
        return

    # 4. 发起批量标注请求
    print(f"\n开始批量标注...")
    response = requests.post(
        f"{API_BASE}/annotate/",
        json={"image_ids": unannotated_ids},
        timeout=300,  # 5 分钟超时
    )

    result = response.json()
    print(f"\n响应状态码: {response.status_code}")
    print(f"消息: {result.get('message')}")

    # 5. 统计结果
    success_count = sum(1 for r in result["results"] if r["success"])
    failed_count = len(result["results"]) - success_count

    print(f"\n结果统计:")
    print(f"  成功: {success_count}")
    print(f"  失败: {failed_count}")

    # 6. 显示失败详情
    if failed_count > 0:
        print(f"\n失败详情:")
        for r in result["results"]:
            if not r["success"]:
                print(f"  - {r['image_id']}: {r['message']}")


if __name__ == "__main__":
    print("标注功能测试")
    print("=" * 60)

    # 测试 1: 单张图片标注
    test_single_annotation()

    # 测试 2: 批量标注（10 张）
    # test_batch_annotation(10)

    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)
    print("\n提示:")
    print("1. 查看后端日志，应该看到详细的标注过程")
    print("2. 如果标注失败，日志会显示具体原因")
    print("3. 超时时间已增加到 120 秒，应该能处理更多图片")
    print("4. 如果单张图片标注失败，会自动重试最多 3 次")
