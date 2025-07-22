class ProductClassificationApp(ttk.Frame):
    def __init__(self, parent):
        # 初始化父类Frame
        super().__init__(parent)
        self.pack(fill=BOTH, expand=True)
        
        # 保存父组件引用
        self.parent = parent
        
        # 检查时间验证
        if not self.check_expiration():
            messagebox.showerror("错误", "DLL注册失败，请联系Cayman Fu 13111986898", parent=self.winfo_toplevel())
            return
        
        # 创建主框架
        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.pack(fill=BOTH, expand=True)
        
        # 创建控制面板
        self.create_control_panel()
        
        # 创建日志显示区域
        self.create_log_area()
        
        # 初始化状态
        self.processing = False
        self.file_list = []
        self.file_path = StringVar()
        self.file_mode = StringVar(value="multi_files")