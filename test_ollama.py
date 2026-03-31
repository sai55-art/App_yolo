import asyncio
import sys

sys.path.insert(0, ".")

from backend.services.ollama_vision import OllamaVisionService
from pathlib import Path


async def test_single_image():
    service = OllamaVisionService()

    images_dir = Path("data/images")
    test_image = list(images_dir.glob("*.jpg"))[0]

    print(f"测试图片：{test_image}")
    print("开始标注...")

    annotation = await service.annotate_image(test_image)

    print(f"\n标注结果:")
    print(f"对象数量：{len(annotation.get('objects', []))}")

    for obj in annotation.get("objects", []):
        print(
            f"  - {obj['class']}: confidence={obj['confidence']:.2f}, bbox={obj['bbox']}"
        )

    return annotation


if __name__ == "__main__":
    result = asyncio.run(test_single_image())
