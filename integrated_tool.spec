# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Integrated_Tool.py'],
    pathex=[],
    binaries=[],
    datas=[('config.txt', '.'), ('favicon.ico', '.')],
    hiddenimports=['pandas', 'openpyxl', 'xlrd', 'xlwt', 'xlsxwriter', 'numpy', 'tkinter', 'tkinter.ttk', 'tkinter.messagebox', 'tkinter.filedialog', 'tkinter.font', 'tkinter.scrolledtext', 'tkinter.tix', 'tkinter.constants', 'tkinter.dnd', 'tkinter.colorchooser', 'tkinter.commondialog', 'tkinter.dialog', 'tkinter.filedialog', 'tkinter.font', 'tkinter.messagebox', 'tkinter.scrolledtext', 'tkinter.tix', 'tkinter.ttk', 'tkinter.constants', 'tkinter.dnd', 'tkinter.colorchooser', 'tkinter.commondialog', 'tkinter.dialog', 'tkinter.filedialog', 'tkinter.font', 'tkinter.messagebox', 'tkinter.scrolledtext', 'tkinter.tix', 'tkinter.ttk'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    resources=['app.res'],
    name='Supplier_Reconciliation_Tools',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='favicon.ico',
)