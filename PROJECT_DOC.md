# YOLO + Llava 混合自动标注系统

## 环境配置
- **技术栈**: Python
- **环境管理**: conda
- **环境名称**: yolo_use
- **激活命令**: `conda activate yolo_use`

## 项目目标
实现 YOLO + Llava 混合自动标注方案：
- YOLO 检测苹果位置（精确边界框）
- Llava 判断苹果状态（正常/有缺陷）
- 生成高质量 YOLO 格式标注数据

## 阶段规划

### Phase 1: YOLO 水果检测服务 ✅ 完成
- [x] 创建检测服务 `services/yolo_detector.py`
- [x] 封装检测接口
- [x] API 集成 `/api/v1/detect/`
- [x] 测试验证

### Phase 2: Llava 苹果分类服务 ✅ 完成
- [x] 裁剪苹果区域功能 `services/fruit_cropper.py`
- [x] Llava 分类接口 `services/fruit_classifier.py`
- [x] 整合服务 `services/hybrid_annotator.py`
- [x] 新 API `/api/v1/annotate/hybrid/`

### Phase 3: 整合自动标注流程 ✅ 完成
- [x] 测试混合标注 API
- [x] 边界框准确性验证
- [x] 分类功能验证
- [x] 标注文件格式正确

### Phase 4: 模型转换功能 ✅ 完成
- [x] 4.1 启用 trainer.py 自动转换代码
- [x] 4.2 修复 docker-compose.yml 镜像名
- [x] 4.3 验证 ONNX 转换 (本地)
- [x] 4.4 验证 cvimodel 转换 (Docker)
- [x] 4.5 地平线 mud (目标设备是 MaixCAM，不需要)
- [x] 4.6 前端整合 cvimodel 下载
- [x] 4.7 添加删除模型功能

## 模型转换

### 已验证格式
| 格式 | 平台 | 状态 |
|------|------|------|
| PT | PyTorch | ✅ 原始格式 |
| ONNX | 通用中间格式 | ✅ 已验证 |
| cvimodel | MaixCAM (CV186x) | ✅ 已验证 |
| mud | 地平线 Horizon X3 | ⏭️ 不需要 |

### 转换流程
```
best.pt → best.onnx → best.cvimodel / best.mud
```

### Docker 镜像
```bash
# ONNX (本地已验证，无需 Docker)
# cvimodel 转换
docker pull sophgo/tpuc_dev:v3.4

# mud 转换需要地平线授权
```

### cvimodel 转换命令
```bash
# 启动容器
docker run -it --rm -v D:/pycharm/apple/models/converted:/workspace/models sophgo/tpuc_dev:v3.4 bash

# 安装 tpu-mlir
pip install tpu-mlir onnx -i https://pypi.tuna.tsinghua.edu.cn/simple

# ONNX → MLIR
model_transform --model_name best --model_def best.onnx --input_shapes "[[1,3,640,640]]" --mean "0,0,0" --scale "1,1,1" --output . --mlir best.mlir --output_names output0

# MLIR → cvimodel (CV186x)
model_deploy --mlir best.mlir --chip cv186x --model best.cvimodel --quantize F32
```

## 模型选择