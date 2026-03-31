# -*- coding: utf-8 -*-
"""
苹果品质检测系统 - 流程图绘制脚本
使用 matplotlib + networkx 绘制6张流程图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

# 输出目录
OUTPUT_DIR = Path("C:/Users/Sai/Desktop/流程图")
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

# 颜色定义
COLORS = {
    "start": "#e1f5fe",
    "process": "#ffffff",
    "ai": "#f3e5f5",
    "storage": "#fff9c4",
    "deploy": "#e8f5e9",
    "end": "#c8e6c9",
    "decision": "#ffcc80",
}


def draw_flowchart_1():
    """绘制主工作流程图"""
    fig, ax = plt.subplots(figsize=(14, 18))
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 20)
    ax.axis("off")
    ax.set_title(
        "苹果品质检测系统 - 主工作流程图", fontsize=16, fontweight="bold", pad=20
    )

    nodes = [
        (5, 19, "用户上传图片", COLORS["start"]),
        (5, 17, "图片存储与管理", COLORS["process"]),
        (5, 15, "调用Ollama大模型", COLORS["ai"]),
        (5, 13, "自动智能标注", COLORS["ai"]),
        (5, 11, "标注结果检查", COLORS["decision"]),
        (2, 9, "人工修正", COLORS["process"]),
        (5, 7, "构建YOLO数据集", COLORS["process"]),
        (5, 5, "YOLOv11m模型训练", COLORS["ai"]),
        (5, 3, "模型推理测试", COLORS["process"]),
        (5, 1, "MQTT发布部署", COLORS["deploy"]),
        (5, -1, "摄像头设备更新", COLORS["end"]),
    ]

    for x, y, text, color in nodes:
        if "检查" in text:
            diamond = mpatches.RegularPolygon(
                (x, y),
                numVertices=4,
                radius=0.8,
                orientation=np.pi / 4,
                facecolor=color,
                edgecolor="black",
                linewidth=1.5,
            )
            ax.add_patch(diamond)
        else:
            rect = FancyBboxPatch(
                (x - 1.5, y - 0.4),
                3,
                0.8,
                boxstyle="round,pad=0.05,rounding_size=0.2",
                facecolor=color,
                edgecolor="black",
                linewidth=1.5,
            )
            ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=10, fontweight="bold")

    arrows = [
        (5, 18.6, 5, 17.4),
        (5, 16.6, 5, 15.4),
        (5, 14.6, 5, 13.4),
        (5, 12.6, 5, 11.4),
        (4.2, 10.6, 2, 9.4),
        (5.8, 10.6, 5, 7.4),
        (2, 8.6, 5, 7.4),
        (5, 6.6, 5, 5.4),
        (5, 4.6, 5, 3.4),
        (5, 2.6, 5, 1.4),
        (5, 0.6, 5, -0.6),
    ]

    for x1, y1, x2, y2 in arrows:
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="->", color="#333333", lw=1.5),
        )

    ax.text(3, 10.3, "不满意", fontsize=9, color="red", fontweight="bold")
    ax.text(6, 10.3, "满意", fontsize=9, color="green", fontweight="bold")

    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "01_主工作流程图.png",
        dpi=150,
        bbox_inches="tight",
        facecolor="white",
        edgecolor="none",
    )
    plt.close()
    print("[OK] 已生成: 01_主工作流程图.png")


def draw_flowchart_2():
    """绘制系统架构图"""
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(-1, 12)
    ax.axis("off")
    ax.set_title(
        "苹果品质检测系统 - 系统架构图", fontsize=16, fontweight="bold", pad=20
    )

    layers = [
        (10.5, "用户层", ["Web管理界面"], "#bbdefb"),
        (8.5, "应用层", ["FastAPI后端服务", "WebSocket实时通信"], "#c8e6c9"),
        (
            6,
            "服务层",
            ["上传服务", "标注服务", "训练服务", "推理服务", "部署服务"],
            "#fff9c4",
        ),
        (3.5, "AI模型层", ["YOLOv11m", "Ollama qwen2.5vl", "模型转换器"], "#f8bbd9"),
        (1.5, "通信层", ["MQTT Broker", "HTTP文件服务"], "#c5e1a5"),
    ]

    for y, name, components, color in layers:
        rect = FancyBboxPatch(
            (0.5, y - 0.8),
            11,
            1.6,
            boxstyle="round,pad=0.05",
            facecolor=color,
            edgecolor="#666666",
            linewidth=2,
            alpha=0.3,
        )
        ax.add_patch(rect)

        ax.text(
            0.8,
            y,
            name,
            ha="left",
            va="center",
            fontsize=11,
            fontweight="bold",
            color="#333333",
        )

        start_x = 3
        for j, comp in enumerate(components):
            cx = start_x + j * 2
            rect = FancyBboxPatch(
                (cx - 0.9, y - 0.35),
                1.8,
                0.7,
                boxstyle="round,pad=0.02",
                facecolor="white",
                edgecolor="#333333",
                linewidth=1,
            )
            ax.add_patch(rect)
            ax.text(cx, y, comp, ha="center", va="center", fontsize=9)

    rect = FancyBboxPatch(
        (2.5, -0.5),
        9,
        1,
        boxstyle="round,pad=0.05",
        facecolor="#e1bee7",
        edgecolor="#666666",
        linewidth=2,
        alpha=0.3,
    )
    ax.add_patch(rect)
    ax.text(
        2.8,
        0,
        "存储层",
        ha="left",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="#333333",
    )

    storage = ["图片存储", "标注存储", "模型存储", "JSON注册表"]
    for j, s in enumerate(storage):
        sx = 4.5 + j * 2
        rect = FancyBboxPatch(
            (sx - 0.8, -0.35),
            1.6,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="white",
            edgecolor="#333333",
            linewidth=1,
        )
        ax.add_patch(rect)
        ax.text(sx, 0, s, ha="center", va="center", fontsize=9)

    rect = FancyBboxPatch(
        (13, 8),
        2.5,
        1.5,
        boxstyle="round,pad=0.1",
        facecolor="#ffcc80",
        edgecolor="#333333",
        linewidth=2,
    )
    ax.add_patch(rect)
    ax.text(
        14.25,
        8.75,
        "摄像头设备\nMaixCAM",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
    )

    ax.annotate(
        "",
        xy=(6, 9.3),
        xytext=(6, 10.2),
        arrowprops=dict(arrowstyle="<->", color="#666666", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(6, 6.8),
        xytext=(6, 8.2),
        arrowprops=dict(arrowstyle="->", color="#666666", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(6, 4.3),
        xytext=(6, 5.2),
        arrowprops=dict(arrowstyle="->", color="#666666", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(6, 2.3),
        xytext=(6, 3.2),
        arrowprops=dict(arrowstyle="->", color="#666666", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(13, 8.75),
        xytext=(11.5, 1.5),
        arrowprops=dict(
            arrowstyle="->", color="#666666", lw=1.5, connectionstyle="arc3,rad=0.2"
        ),
    )

    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "02_系统架构图.png",
        dpi=150,
        bbox_inches="tight",
        facecolor="white",
        edgecolor="none",
    )
    plt.close()
    print("[OK] 已生成: 02_系统架构图.png")


def draw_flowchart_3():
    """绘制自动标注流程图"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("自动标注流程图", fontsize=16, fontweight="bold", pad=20)

    participants = [
        (1, "用户"),
        (4, "前端"),
        (7, "后端API"),
        (10, "Ollama"),
        (13, "存储"),
    ]

    for x, name in participants:
        rect = FancyBboxPatch(
            (x - 0.8, 9),
            1.6,
            0.6,
            boxstyle="round,pad=0.05",
            facecolor="#e3f2fd",
            edgecolor="#1976d2",
            linewidth=2,
        )
        ax.add_patch(rect)
        ax.text(x, 9.3, name, ha="center", va="center", fontsize=11, fontweight="bold")
        ax.plot([x, x], [0.5, 9], "k--", lw=1, alpha=0.3)

    steps = [
        (1, 8, 4, 8, "选择图片"),
        (4, 7, 7, 7, "POST /api/v1/annotate/"),
        (7, 6, 13, 6, "读取图片"),
        (13, 5.5, 7, 5.5, "返回图片数据"),
        (7, 4.5, 10, 4.5, "发送图片+提示词"),
        (10, 3.5, 10, 3.5, "分析图片内容"),
        (10, 2.5, 7, 2.5, "返回JSON标注"),
        (7, 2, 13, 2, "保存标注文件"),
        (7, 1.5, 4, 1.5, "返回标注结果"),
        (4, 1, 1, 1, "显示标注信息"),
    ]

    for x1, y1, x2, y2, text in steps:
        if x1 == x2:
            rect = FancyBboxPatch(
                (x1, y1 - 0.3),
                1.5,
                0.6,
                boxstyle="round,pad=0.02",
                facecolor="#fff9c4",
                edgecolor="#f57c00",
                linewidth=1,
            )
            ax.add_patch(rect)
            ax.text(x1 + 0.75, y1, text, ha="center", va="center", fontsize=8)
        else:
            color = "#2196f3" if x2 > x1 else "#4caf50"
            ax.annotate(
                "",
                xy=(x2, y2),
                xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=color, lw=1.5),
            )
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 + 0.2
            ax.text(
                mid_x,
                mid_y,
                text,
                ha="center",
                va="bottom",
                fontsize=9,
                bbox=dict(
                    boxstyle="round,pad=0.2",
                    facecolor="white",
                    edgecolor="none",
                    alpha=0.8,
                ),
            )

    rect = FancyBboxPatch(
        (9, 3.2),
        2,
        1,
        boxstyle="round,pad=0.05",
        facecolor="#fff9c4",
        edgecolor="#f57c00",
        linewidth=1.5,
    )
    ax.add_patch(rect)
    ax.text(
        10, 3.7, "分析图片\n检测苹果\n判断类别", ha="center", va="center", fontsize=8
    )

    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "03_自动标注流程图.png",
        dpi=150,
        bbox_inches="tight",
        facecolor="white",
        edgecolor="none",
    )
    plt.close()
    print("[OK] 已生成: 03_自动标注流程图.png")


def draw_flowchart_4():
    """绘制模型训练流程图"""
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis("off")
    ax.set_title("模型训练流程图", fontsize=16, fontweight="bold", pad=20)

    phases = [
        (2, 10, "准备阶段", "#e3f2fd"),
        (6, 10, "配置阶段", "#fff9c4"),
        (10, 10, "训练阶段", "#f3e5f5"),
        (14, 10, "输出阶段", "#e8f5e9"),
    ]

    for x, y, text, color in phases:
        rect = FancyBboxPatch(
            (x - 1.5, y - 0.3),
            3,
            0.6,
            boxstyle="round,pad=0.05",
            facecolor=color,
            edgecolor="#333333",
            linewidth=2,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=11, fontweight="bold")

    prep_nodes = [
        (2, 8, "选择已标注图片"),
        (2, 6.5, "构建数据集"),
        (2, 5, "划分训练/验证集"),
        (2, 3.5, "生成data.yaml"),
    ]

    for x, y, text in prep_nodes:
        rect = FancyBboxPatch(
            (x - 1.3, y - 0.35),
            2.6,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="white",
            edgecolor="#1976d2",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    for i in range(len(prep_nodes) - 1):
        ax.annotate(
            "",
            xy=(2, prep_nodes[i + 1][1] + 0.35),
            xytext=(2, prep_nodes[i][1] - 0.35),
            arrowprops=dict(arrowstyle="->", color="#1976d2", lw=1.5),
        )

    config_nodes = [
        (5, 8, "设置epochs"),
        (5, 6.5, "设置batch_size"),
        (7, 8, "选择设备"),
        (7, 6.5, "选择基础模型"),
    ]

    for x, y, text in config_nodes:
        rect = FancyBboxPatch(
            (x - 1.2, y - 0.35),
            2.4,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="white",
            edgecolor="#f57c00",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    ax.plot([5, 5, 6, 6], [7.15, 5.5, 5.5, 7.15], "k-", lw=1)
    ax.plot([7, 7, 6, 6], [7.15, 5.5, 5.5, 7.15], "k-", lw=1)

    rect = FancyBboxPatch(
        (5, 4.5),
        2,
        0.7,
        boxstyle="round,pad=0.02",
        facecolor="#fff9c4",
        edgecolor="#f57c00",
        linewidth=1.5,
    )
    ax.add_patch(rect)
    ax.text(6, 4.85, "提交训练任务", ha="center", va="center", fontsize=9)
    ax.annotate(
        "",
        xy=(6, 5.2),
        xytext=(6, 5.5),
        arrowprops=dict(arrowstyle="->", color="#333333", lw=1),
    )

    train_nodes = [
        (10, 8, "初始化YOLOv11m"),
        (10, 6, "加载预训练模型"),
        (10, 4, "训练循环"),
        (10, 2, "WebSocket推送进度"),
    ]

    for x, y, text in train_nodes:
        rect = FancyBboxPatch(
            (x - 1.5, y - 0.35),
            3,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="white",
            edgecolor="#7b1fa2",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    for i in range(len(train_nodes) - 1):
        ax.annotate(
            "",
            xy=(10, train_nodes[i + 1][1] + 0.35),
            xytext=(10, train_nodes[i][1] - 0.35),
            arrowprops=dict(arrowstyle="->", color="#7b1fa2", lw=1.5),
        )

    ax.annotate(
        "",
        xy=(11.8, 6),
        xytext=(11.8, 4),
        arrowprops=dict(
            arrowstyle="->", color="#7b1fa2", lw=1.5, connectionstyle="arc3,rad=-0.5"
        ),
    )
    ax.text(12.2, 5, "循环", fontsize=8, color="#7b1fa2")

    output_nodes = [
        (14, 6, "训练曲线图"),
        (14, 4, "模型权重 best.pt"),
        (14, 2, "注册表更新"),
    ]

    for x, y, text in output_nodes:
        rect = FancyBboxPatch(
            (x - 1.3, y - 0.35),
            2.6,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="#e8f5e9",
            edgecolor="#388e3c",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    for i in range(len(output_nodes) - 1):
        ax.annotate(
            "",
            xy=(14, output_nodes[i + 1][1] + 0.35),
            xytext=(14, output_nodes[i][1] - 0.35),
            arrowprops=dict(arrowstyle="->", color="#388e3c", lw=1.5),
        )

    ax.annotate(
        "",
        xy=(4.5, 4.85),
        xytext=(3.3, 3.5),
        arrowprops=dict(arrowstyle="->", color="#333333", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(8.5, 8),
        xytext=(7, 4.85),
        arrowprops=dict(arrowstyle="->", color="#333333", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(12.7, 6),
        xytext=(11.5, 8),
        arrowprops=dict(arrowstyle="->", color="#333333", lw=1.5),
    )

    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "04_模型训练流程图.png",
        dpi=150,
        bbox_inches="tight",
        facecolor="white",
        edgecolor="none",
    )
    plt.close()
    print("[OK] 已生成: 04_模型训练流程图.png")


def draw_flowchart_5():
    """绘制MQTT部署流程图"""
    fig, ax = plt.subplots(figsize=(14, 11))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 12)
    ax.axis("off")
    ax.set_title("MQTT部署流程图", fontsize=16, fontweight="bold", pad=20)

    participants = [
        (1, "用户"),
        (3.5, "Web界面"),
        (6, "服务器"),
        (8.5, "MQTT\nBroker"),
        (11, "摄像头\n设备"),
    ]

    for x, name in participants:
        rect = FancyBboxPatch(
            (x - 0.9, 11),
            1.8,
            0.7,
            boxstyle="round,pad=0.05",
            facecolor="#e3f2fd",
            edgecolor="#1976d2",
            linewidth=2,
        )
        ax.add_patch(rect)
        ax.text(
            x, 11.35, name, ha="center", va="center", fontsize=10, fontweight="bold"
        )
        ax.plot([x, x], [0.5, 11], "k--", lw=1, alpha=0.3)

    steps = [
        (1, 10, 3.5, 10, "点击部署模型", "#2196f3"),
        (3.5, 9, 6, 9, "POST /deploy/publish", "#2196f3"),
        (6, 8, 11, 8, "查找模型文件", "#ff9800"),
        (6, 7, 11, 7, "计算MD5校验值", "#ff9800"),
        (6, 6, 8.5, 6, "发布MQTT消息", "#4caf50"),
        (8.5, 5, 11, 5, "推送更新通知", "#2196f3"),
        (11, 4, 6, 4, "GET 下载模型", "#2196f3"),
        (6, 3.5, 11, 3.5, "返回模型数据", "#4caf50"),
        (11, 2.5, 11, 2.5, "MD5校验", "#ff9800"),
    ]

    for x1, y1, x2, y2, text, color in steps:
        if x1 == x2:
            rect = FancyBboxPatch(
                (x1 - 0.3, y1 - 0.25),
                1.5,
                0.5,
                boxstyle="round,pad=0.02",
                facecolor="#fff9c4",
                edgecolor="#f57c00",
                linewidth=1,
            )
            ax.add_patch(rect)
            ax.text(x1 + 0.45, y1, text, ha="center", va="center", fontsize=8)
        else:
            arrow_color = "#2196f3" if x2 > x1 else "#4caf50"
            ax.annotate(
                "",
                xy=(x2, y2),
                xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=arrow_color, lw=1.5),
            )
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 + 0.2
            ax.text(
                mid_x,
                mid_y,
                text,
                ha="center",
                va="bottom",
                fontsize=8,
                bbox=dict(
                    boxstyle="round,pad=0.15",
                    facecolor="white",
                    edgecolor="none",
                    alpha=0.9,
                ),
            )

    diamond = mpatches.RegularPolygon(
        (11, 1.5),
        numVertices=4,
        radius=0.5,
        orientation=np.pi / 4,
        facecolor="#ffcc80",
        edgecolor="black",
        linewidth=1.5,
    )
    ax.add_patch(diamond)
    ax.text(11, 1.5, "校验?", ha="center", va="center", fontsize=8, fontweight="bold")

    success_steps = [
        (11, 0.5, "覆盖旧模型"),
    ]

    for x, y, text in success_steps:
        rect = FancyBboxPatch(
            (x - 0.8, y - 0.25),
            1.6,
            0.5,
            boxstyle="round,pad=0.02",
            facecolor="#c8e6c9",
            edgecolor="#388e3c",
            linewidth=1,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=8)

    ax.annotate(
        "",
        xy=(11, 0.75),
        xytext=(11, 1),
        arrowprops=dict(arrowstyle="->", color="#388e3c", lw=1.5),
    )
    ax.text(11.6, 1.7, "成功", fontsize=8, color="#388e3c", fontweight="bold")

    ax.text(
        1,
        0.5,
        "[OK] 部署成功",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="#388e3c",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#e8f5e9", edgecolor="#388e3c"),
    )

    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "05_MQTT部署流程图.png",
        dpi=150,
        bbox_inches="tight",
        facecolor="white",
        edgecolor="none",
    )
    plt.close()
    print("[OK] 已生成: 05_MQTT部署流程图.png")


def draw_flowchart_6():
    """绘制数据流向图"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("数据流向图", fontsize=16, fontweight="bold", pad=20)

    ax.text(
        1.5,
        9.5,
        "输入",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="#e3f2fd", edgecolor="#1976d2"),
    )
    input_nodes = [
        (1.5, 8, "用户上传图片"),
        (1.5, 6.5, "配置参数"),
    ]
    for x, y, text in input_nodes:
        rect = FancyBboxPatch(
            (x - 1, y - 0.35),
            2,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="#bbdefb",
            edgecolor="#1976d2",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    ax.text(
        5,
        9.5,
        "处理",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="#fff9c4", edgecolor="#f57c00"),
    )
    process_nodes = [
        (5, 8, "图片存储"),
        (5, 6.5, "标注生成"),
        (5, 5, "数据集构建"),
        (5, 3.5, "模型训练"),
        (5, 2, "模型转换"),
    ]
    for x, y, text in process_nodes:
        rect = FancyBboxPatch(
            (x - 1.3, y - 0.35),
            2.6,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="white",
            edgecolor="#f57c00",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    ax.text(
        8.5,
        9.5,
        "存储",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="#e1bee7", edgecolor="#7b1fa2"),
    )
    storage_nodes = [
        (8.5, 7.5, "images.json"),
        (8.5, 5.5, "annotations.json"),
        (8.5, 3.5, "trainings.json"),
        (8.5, 1.5, "models/"),
    ]
    for x, y, text in storage_nodes:
        rect = FancyBboxPatch(
            (x - 1.2, y - 0.35),
            2.4,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="#f3e5f5",
            edgecolor="#7b1fa2",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    ax.text(
        12,
        9.5,
        "输出",
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="#c8e6c9", edgecolor="#388e3c"),
    )
    output_nodes = [
        (12, 7.5, "检测结果"),
        (12, 5.5, "训练曲线"),
        (12, 3.5, "部署消息"),
        (12, 1.5, "摄像头更新"),
    ]
    for x, y, text in output_nodes:
        rect = FancyBboxPatch(
            (x - 1, y - 0.35),
            2,
            0.7,
            boxstyle="round,pad=0.02",
            facecolor="#e8f5e9",
            edgecolor="#388e3c",
            linewidth=1.5,
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha="center", va="center", fontsize=9)

    ax.annotate(
        "",
        xy=(3.7, 8),
        xytext=(2.5, 8),
        arrowprops=dict(arrowstyle="->", color="#1976d2", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(3.7, 3.5),
        xytext=(2.5, 6.5),
        arrowprops=dict(arrowstyle="->", color="#1976d2", lw=1.5),
    )

    for i in range(len(process_nodes) - 1):
        ax.annotate(
            "",
            xy=(5, process_nodes[i + 1][1] + 0.35),
            xytext=(5, process_nodes[i][1] - 0.35),
            arrowprops=dict(arrowstyle="->", color="#f57c00", lw=1.5),
        )

    ax.annotate(
        "",
        xy=(7.3, 7.5),
        xytext=(6.3, 8),
        arrowprops=dict(arrowstyle="->", color="#7b1fa2", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(7.3, 5.5),
        xytext=(6.3, 6.5),
        arrowprops=dict(arrowstyle="->", color="#7b1fa2", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(7.3, 3.5),
        xytext=(6.3, 3.5),
        arrowprops=dict(arrowstyle="->", color="#7b1fa2", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(7.3, 1.5),
        xytext=(6.3, 2),
        arrowprops=dict(arrowstyle="->", color="#7b1fa2", lw=1.5),
    )

    ax.annotate(
        "",
        xy=(11, 7.5),
        xytext=(9.7, 3.5),
        arrowprops=dict(
            arrowstyle="->", color="#388e3c", lw=1.5, connectionstyle="arc3,rad=0.2"
        ),
    )
    ax.annotate(
        "",
        xy=(11, 5.5),
        xytext=(9.7, 3.5),
        arrowprops=dict(arrowstyle="->", color="#388e3c", lw=1.5),
    )
    ax.annotate(
        "",
        xy=(11, 3.5),
        xytext=(9.7, 1.5),
        arrowprops=dict(
            arrowstyle="->", color="#388e3c", lw=1.5, connectionstyle="arc3,rad=-0.2"
        ),
    )
    ax.annotate(
        "",
        xy=(11, 1.5),
        xytext=(9.7, 1.5),
        arrowprops=dict(arrowstyle="->", color="#388e3c", lw=1.5),
    )

    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "06_数据流向图.png",
        dpi=150,
        bbox_inches="tight",
        facecolor="white",
        edgecolor="none",
    )
    plt.close()
    print("[OK] 已生成: 06_数据流向图.png")


def main():
    """主函数"""
    print("=" * 50)
    print("开始绘制苹果品质检测系统流程图...")
    print("=" * 50)
    print()

    draw_flowchart_1()
    draw_flowchart_2()
    draw_flowchart_3()
    draw_flowchart_4()
    draw_flowchart_5()
    draw_flowchart_6()

    print()
    print("=" * 50)
    print(f"[OK] 所有流程图已生成!")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    print("=" * 50)


if __name__ == "__main__":
    main()
