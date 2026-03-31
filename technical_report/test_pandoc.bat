@echo off
echo 正在转换技术报告为 Word 文档...
pandoc "苹果品质检测系统技术报告.md" -o "苹果品质检测系统技术报告.docx" --toc --toc-depth=3 -V lang=zh-CN

if %errorlevel% equ 0 (
    echo 转换成功！生成的 Word 文档: 苹果品质检测系统技术报告.docx
) else (
    echo 转换失败，请检查 pandoc 是否已安装
    echo 安装 pandoc: https://pandoc.org/installing.html
)
pause