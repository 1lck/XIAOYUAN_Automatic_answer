# 使用说明文档

# 标题页
- 项目名称: 基于OCR的小猿口算自动化脚本
- 版本号: V1.0
- 发布日期: 2024年10月10日
- 编写者/贡献者名单: 后端：李陈康 | 测试：H₂O

# 简介
## 项目背景
本项目旨在通过Python语言实现一个自动化的流程，能够自动识别文本、计算答案，并自动提交答案至下一题。

## 项目目标
提高计算题目的效率，使得用户能够在短时间内完成更多的题目，提高便捷性。

## 目标受众
所有希望利用此工具提高解题速度的用户。

# 安装指南
## 系统要求
- Python版本需至少为3.0.7及以上版本。

## 安装步骤
1. 确保您的计算机已安装Python。
2. 安装所需的第三方库，包括但不限于`pyautogui`, `pygetwindow`, `pytesseract`, `PIL`等。
3. 下载并配置Tesseract OCR引擎。
4. 解压或克隆本项目至本地文件夹。
5. 修改代码中的Tesseract路径设置（如需）。
6. 运行脚本。

## 配置环境
- 安装必要的库：`pip install pytesseract pyautogui pygetwindow pillow`

# 使用说明
## 功能概述
这是一个集成了OCR识别技术的自动刷题系统，可以识别题目、计算答案，并自动提交答案进入下一题。

## 操作流程
1. 确认“雷电模拟器”窗口已打开并处于激活状态。
2. 运行脚本文件。
3. 脚本将自动开始识别、计算并提交答案。

# 开发者指南
## 开发环境搭建
- 创建Python虚拟环境。
- 安装必要的开发库。
- 配置开发工具（如IDE）。

## 代码结构
- 识别模块: 使用OCR技术识别题目中的数字。
- 算法模块: 对识别出的数字进行比较计算。
- 作答操作模块: 控制鼠标移动和点击以输入答案。
- 延迟函数: 控制自动进入下一题的时间间隔。

## 贡献指南
暂无具体贡献指南。

# 故障排除
## 常见问题及解决办法
1. 没有导入相关库
   - 确保所有必要的库都已安装。
2. 没有更改窗口名
   - 修改代码中的窗口名称匹配实际使用的窗口名称。
3. 窗口名不完整
   - 确保窗口名称完全一致。

# 联系我们
- 微信: a0517lck

# 致谢
感谢以下人员对本项目的贡献和支持：
- 李陈康
- 黄浩

# 版权声明
- 本项目仅供学习交流使用，禁止任何商业用途。开发者可以在此基础上进行二次开发，但需保留原作者信息。
