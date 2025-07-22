import pandas as pd
import warnings
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.page import PageMargins
from openpyxl.worksheet.properties import WorksheetProperties, PageSetupProperties
from datetime import datetime
import os
from tkinter import *
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import threading
import shutil
import sys
import subprocess
from Product_Classification_Tool import ProductClassificationApp

class BldBuyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("供应商对帐工具集")
        
        # 设置窗口大小并居中
        self.set_window_geometry(800, 628)
        
        # 创建主题选择下拉框
        self.create_theme_selector()
        
        # 使窗口前台显示
        self.bring_to_front()
        
        # 检查时间验证
        self.check_expiration()
        
        # 检查并确保配置文件存在
        self.ensure_config_file()
            
        # 定义期望的表头字段
        self.expected_headers = [
            "收货日期", "订单号", "商品名称", "实收数量", "基本单位",
            "单价(结算)", "小计金额(结算)", "税额(结算)", "小计价税(结算)", "部门",
            "税率", "供应商/备用金报销账户","商品分类"
        ]
        
        # 创建主框架
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=BOTH, expand=True)
        
        # 创建左右分割的布局
        self.paned_window = ttk.PanedWindow(self.main_frame, orient=HORIZONTAL, bootstyle=PRIMARY)
        self.paned_window.pack(fill=BOTH, expand=True)
        
        # 创建左侧功能按钮区域
        self.left_frame = ttk.Frame(self.paned_window, padding="5")
        self.paned_window.add(self.left_frame, weight=1)
        
        # 创建右侧操作区域
        self.right_frame = ttk.Frame(self.paned_window, padding="5")
        self.paned_window.add(self.right_frame, weight=4)
        
        # 创建左侧功能按钮
        self.create_left_buttons()
        
        # 创建右侧控制面板
        self.create_control_panel()
        
        # 创建日志显示区域
        self.create_log_area()
        
        # 初始化状态
        self.processing = False