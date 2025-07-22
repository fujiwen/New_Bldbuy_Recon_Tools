# 供应商对账工具集

这是一个用于处理供应商对账明细的工具集，主要功能包括：

- 处理收货单商品明细数据
- 自动识别表头和数据
- 按供应商分组处理数据
- 生成标准格式的对账单
- 支持批量处理多个文件
- 自动归档已处理文件

## 系统要求

- Python 3.10 或更高版本
- Windows 操作系统

## 依赖包

- pandas >= 2.0.0
- numpy >= 1.24.0
- openpyxl >= 3.1.0
- xlrd >= 2.0.0
- Pillow >= 10.0.0
- tk >= 0.1.0
- pyinstaller >= 6.0.0

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/fujiwen/New_Bldbuy_Recon_Tools.git
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 运行程序：
```bash
python Integrated_Tool.py
```

2. 在界面中选择要处理的Excel文件
3. 点击"开始处理"按钮
4. 处理完成后，可以在export文件夹中找到生成的对账单

## 配置文件

程序使用config.txt配置文件来设置对账单的表头信息，包括：

- 酒店名称
- 地址
- 联系人信息
- 表格标题

## 自动构建

本项目使用GitHub Actions自动构建Windows可执行文件。每次推送到main分支时，都会自动触发构建流程，生成新的可执行文件。