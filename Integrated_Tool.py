import sys
from Bldbuy_Recon_UI import BldBuyApp
from tkinter import Tk
import ttkbootstrap as ttk

def main():
    root = ttk.Window(
        title="供应商对账工具集",
        themename="sandstone",
        size=(800, 628),
        resizable=(True, True),
    )
    app = BldBuyApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()