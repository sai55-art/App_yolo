"""
测试训练功能
"""

import sys

sys.path.insert(0, ".")

from backend.services.trainer import trainer
from pathlib import Path

data_yaml = Path("data/dataset/data.yaml")

print("开始测试训练...")
print(f"数据集配置：{data_yaml}")

if not data_yaml.exists():
    print("错误：data.yaml 不存在")
    sys.exit(1)

train_id = trainer.create_training_task(
    data_yaml=data_yaml, epochs=10, batch_size=8, img_size=640, model_name="yolo11m.pt"
)

print(f"训练任务 ID: {train_id}")
print("开始训练（10 个 epoch）...")


def progress_callback(progress):
    print(
        f"  Epoch {progress['epoch']}/{progress['total_epochs']} - Loss: {progress['loss']:.4f}, mAP: {progress['map']:.4f}"
    )


try:
    result = trainer.train(
        train_id=train_id,
        data_yaml=data_yaml,
        epochs=10,
        batch_size=8,
        img_size=640,
        model_name="yolo11m.pt",
        device="cpu",
        progress_callback=progress_callback,
    )

    print(f"\n训练完成!")
    print(f"状态：{result.status}")
    print(f"模型路径：{result.model_path}")

except Exception as e:
    print(f"\n训练失败：{e}")
    import traceback

    traceback.print_exc()
