"""
测试上传功能
"""

import requests

# 测试文件
test_file = "data/images/20260307_102529_img_1772850329966_6a549f9f.jpg"

print("测试上传功能...")
print(f"文件：{test_file}")

try:
    with open(test_file, "rb") as f:
        files = {"files": f}
        response = requests.post("http://localhost:8000/api/v1/upload/", files=files)

    print(f"状态码：{response.status_code}")
    print(f"响应：{response.json()}")

    if response.status_code == 200:
        print("✅ 上传成功！")
    else:
        print(f"❌ 上传失败：{response.status_code}")

except Exception as e:
    print(f"❌ 错误：{e}")
