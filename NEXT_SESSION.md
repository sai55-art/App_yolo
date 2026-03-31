# Apple YOLO 检测系统 - 下次会话指南

## 当前进度

✅ Phase 1: YOLO 水果检测服务 (已完成)
✅ Phase 2: Llava 苹果分类服务 (已完成)
✅ Phase 3: 混合标注流程 (已完成)
✅ Phase 4: 模型转换功能 (已完成)

---

## 项目已全部完成！

### 功能清单

| 功能 | 状态 | 说明 |
|------|------|------|
| YOLO 检测 | ✅ | 苹果位置检测 |
| Llava 分类 | ✅ | 苹果状态判断 |
| 混合标注 | ✅ | 自动生成标注 |
| 模型训练 | ✅ | 支持增量学习 |
| ONNX 转换 | ✅ | 通用中间格式 |
| cvimodel 转换 | ✅ | MaixCAM 部署 |
| 自动转换 | ✅ | 训练后自动转换 cvimodel |
| 前端下载 | ✅ | 支持 PT + cvimodel 下载 |
| 删除模型 | ✅ | 删除训练记录和文件 |

---

## 模型转换结果

### 最终输出

| 文件 | 大小 | 格式 | 用途 |
|------|------|------|------|
| best.pt | ~40 MB | PyTorch | GPU 训练/推理 |
| best.onnx | 76.71 MB | ONNX | 通用中间格式 |
| best.cvimodel | 82.5 MB | cvimodel | MaixCAM 部署 |

### 自动转换流程

```
训练完成 → ONNX (本地) → cvimodel (Docker)
```

训练完成后自动执行，无需手动操作。

---

## 前端功能

### 训练历史
- 显示训练状态、mAP、Loss
- 继续训练（增量学习）
- **删除训练**（删除记录和文件）

### 模型传出
- 选择训练任务传出
- 显示 PT 下载链接
- **显示 cvimodel 下载链接**（MaixCAM 部署）

---

## API 端点

| 端点 | 方法 | 功能 |
|------|------|------|
| `/api/v1/train/` | POST | 开始训练 |
| `/api/v1/train/` | GET | 训练历史 |
| `/api/v1/train/{id}` | DELETE | **删除训练** |
| `/api/v1/deploy/model/{id}/formats` | GET | 获取可用格式 |
| `/api/v1/deploy/model/{id}/best.pt` | GET | 下载 PT |
| `/api/v1/deploy/model/{id}/best.cvimodel` | GET | 下载 cvimodel |

---

## 环境信息

| 项目 | 信息 |
|------|------|
| **环境** | conda `yolo_use` |
| **激活命令** | `conda activate yolo_use` |
| **项目路径** | `D:\pycharm\apple` |
| **PyTorch** | 2.7.1+cu128 |
| **显卡** | 12GB 显存, CUDA 可用 |
| **Docker** | 29.1.3 (需 TUN 模式) |

---

## Docker 配置要点

### 代理配置

1. **开启 Clash Verge TUN 模式**
2. **关闭 Docker Desktop 的 Manual Proxy**
3. 重启 Docker Desktop

---

## 启动命令

```powershell
conda activate yolo_use
cd D:\pycharm\apple
python -m uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
```

---

## 下一步计划

详见 `docs/MIXED_DEPLOY_PLAN.md` - 混合方案待办清单

### 混合方案架构
```
本地训练 → SSH 上传到 xkur 服务器 → MaixCAM 自主下载
```

### 待办任务
- [ ] xkur 服务器配置 nginx (端口 8090)
- [ ] 创建 `model_uploader.py` 上传服务
- [ ] 修改 `trainer.py` 自动上传
- [ ] 修改 MQTT 消息发送服务器 URL
- [ ] MaixCAM 设备端 MQTT 订阅

---

## Git 提交历史

```
05fcfd3 feat: 训练自动转换cvimodel + 前端下载cvimodel + 删除模型功能
0d72a7d feat: Phase 4 完成，模型转换功能全部就绪
f502dbc feat: 验证 cvimodel 转换成功 (Docker + TPU-MLIR)
9b30096 feat: 启用模型转换功能，验证 ONNX 转换成功
```