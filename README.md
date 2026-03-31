# 🍎 苹果品质检测系统

> **创新混合标注方案**：YOLO 精确定位 + Qwen 智能分类

---

## 🌟 核心亮点：混合标注

### 问题背景

传统自动标注方案存在以下痛点：

| 方案 | 优点 | 缺点 |
|------|------|------|
| 纯大模型标注 | 能理解语义 | 边界框不精确，位置漂移 |
| 纯 YOLO 检测 | 定位精准 | 无法判断苹果是否正常 |
| 人工标注 | 准确可靠 | 成本高、效率低 |

### 我们的方案

**混合标注** = YOLO 精确定位 + Qwen 智能分类

```
┌─────────────┐      ┌─────────────┐
│   原始图片   │ ──→  │  YOLO 检测  │
└─────────────┘      └──────┬──────┘
                            │
                     检测苹果位置（精确边界框）
                            │
                            ▼
                     ┌─────────────┐
                     │  裁剪苹果区域 │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │ Qwen 分类   │
                     └──────┬──────┘
                            │
                    判断正常/有缺陷
                            │
                            ▼
                     ┌─────────────┐
                     │ 最终标注结果 │
                     └─────────────┘
```

### 创新优势

| 优势 | 说明 |
|------|------|
| 🎯 **精确定位** | YOLO 模型专注目标检测，边界框准确 |
| 🧠 **智能分类** | Qwen 视觉模型理解苹果状态，区分正常/瑕疵 |
| 💰 **降低成本** | 自动标注减少 80%+ 人工工作量 |
| ⚡ **提高效率** | 批量处理，无需逐张人工标注 |

### 标注模式

系统支持两种标注模式：

| 模式 | 说明 | 适用场景 |
|------|------|---------|
| 单苹果模式 | 每张图只标注一个苹果 | 单目标图片 |
| 多苹果模式 | 检测图中所有苹果 | 多目标图片 |

---

## 📖 项目简介

基于 FastAPI + YOLOv11 + Ollama 的苹果品质检测平台，支持从数据上传、自动标注、训练、推理到 MQTT 模型发布的完整流程。

### 核心功能

| 功能模块 | 说明 |
|---------|------|
| 📤 图片上传 | 批量上传、拖拽上传、分组管理 |
| 🏷️ 自动标注 | Ollama 视觉模型自动生成 YOLO 格式标注 |
| 🔀 混合标注 | YOLO 定位 + Qwen 分类，兼顾精度与智能 |
| 🎯 模型训练 | YOLOv11 训练，支持增量学习、实时进度监控 |
| 🔍 模型推理 | 单张/批量推理，可视化结果 |
| 📡 MQTT 部署 | 远程推送模型更新到边缘设备 |

### 工作流程

```text
上传图片 → 自动标注 → 人工抽检 → 模型训练 → 推理验证 → MQTT 发布
```

---

## 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| 后端 | FastAPI + Uvicorn |
| 前端 | HTML5 + CSS3 + JavaScript |
| 目标检测 | YOLOv11 (Ultralytics) |
| 视觉理解 | Ollama + Qwen2.5-VL |
| 通信协议 | MQTT + WebSocket |
| 部署 | Docker |

---

## 📁 目录结构

```text
apple/
├── backend/                 # FastAPI 后端
│   ├── app.py               # 应用入口
│   ├── api/                 # 路由层
│   ├── services/            # 业务服务
│   │   ├── hybrid_annotator.py   # 混合标注核心
│   │   ├── yolo_detector.py      # YOLO 检测
│   │   ├── fruit_classifier.py   # Qwen 分类
│   │   └── trainer.py            # 模型训练
│   ├── utils/               # 工具函数
│   └── config.py            # 配置加载
├── frontend/                # 前端模板与静态资源
│   ├── templates/           # HTML 模板
│   └── static/              # CSS/JS
├── configs/                 # 配置文件
│   ├── settings.yaml        # 应用配置
│   ├── mqtt.yaml            # MQTT 配置
│   └── deploy.yaml          # 部署配置
├── docs/                    # 项目文档
├── docker/                  # Docker 配置
├── scripts/                 # 工具脚本
├── tests/                   # 测试代码
├── requirements.txt         # Python 依赖
└── README.md
```

---

## 🚀 快速开始

### 环境要求

- Python 3.11+
- CUDA（可选，用于 GPU 训练）
- Ollama

### 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/sai55-art/App_yolo.git
cd App_yolo
```

2. **创建虚拟环境**

```bash
conda create -n apple_yolo python=3.11 -y
conda activate apple_yolo
pip install -r requirements.txt
```

3. **安装 Ollama 并下载模型**

```bash
# 安装 Ollama: https://ollama.ai/
ollama pull qwen2.5vl:7b
ollama serve
```

4. **下载 YOLO 基础模型**

```bash
# 模型会自动下载，或手动放入 models/ 目录
# 推荐: yolo11m.pt
```

5. **配置文件**

根据需要修改 `configs/` 目录下的配置文件。

6. **启动服务**

```bash
python -m uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
```

7. **访问应用**

- 首页: http://localhost:8000
- API 文档: http://localhost:8000/docs

---

## 📡 API 接口

### 上传管理

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/v1/upload/` | POST | 上传图片 |
| `/api/v1/upload/list` | GET | 获取图片列表 |
| `/api/v1/upload/grouped` | GET | 按日期分组获取 |

### 标注管理

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/v1/annotate/` | POST | 自动标注 |
| `/api/v1/annotate/hybrid/` | POST | 混合标注（推荐）|
| `/api/v1/annotate/list` | GET | 获取标注列表 |

### 模型训练

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/v1/train/` | POST | 开始训练 |
| `/api/v1/train/` | GET | 训练历史 |
| `/api/v1/train/{train_id}/ws` | WS | 实时进度 |

### 模型推理

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/v1/predict/` | POST | 模型推理 |
| `/api/v1/predict/upload` | POST | 上传推理 |

### 模型部署

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/v1/deploy/publish` | POST | MQTT 发布 |
| `/api/v1/deploy/history` | GET | 部署历史 |

---

## 🧪 测试

```bash
pytest tests/ -v
```

---

## 🐛 常见问题

### 1. 自动标注失败

- 检查 Ollama 服务是否运行: `ollama serve`
- 检查模型是否安装: `ollama list`

### 2. 训练失败

- 确认已上传图片并完成标注
- 检查 GPU 内存是否充足

### 3. MQTT 发布失败

- 检查 `configs/mqtt.yaml` 配置
- 使用 `/api/v1/deploy/test-mqtt` 测试连接

---

## 📄 许可证

MIT License

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**最后更新**: 2026-03-30