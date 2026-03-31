"""
测试 yolo11m.pt 模型加载
"""

try:
    from ultralytics import YOLO
    import sys

    print("=" * 50)
    print("测试 YOLO11m 模型加载")
    print("=" * 50)

    model_path = "models/yolo11m.pt"
    print(f"\n正在加载模型：{model_path}...")

    model = YOLO(model_path)

    print(f"✅ 模型加载成功！")
    print(f"   模型类型：{model.type}")
    print(f"   模型任务：{model.task}")
    print(
        f"   类别数量：{model.model[-1].nc if hasattr(model.model[-1], 'nc') else '未知'}"
    )

    # 测试推理
    print("\n正在测试推理...")
    import numpy as np
    from PIL import Image

    # 创建测试图片
    test_img = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
    results = model(test_img, verbose=False)

    print(f"✅ 推理测试成功！")
    print(
        f"   检测结果数：{len(results[0].boxes) if results[0].boxes is not None else 0}"
    )

    print("\n" + "=" * 50)
    print("模型已准备好用于训练！")
    print("=" * 50)

except Exception as e:
    print(f"\n❌ 测试失败：{e}")
    import traceback

    traceback.print_exc()
    sys.exit(1)
