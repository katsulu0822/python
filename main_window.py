# -*- coding: utf-8 -*-
# A視窗 - main_window.py
import tkinter as tk
import window_b_2  # 匯入視窗B模組

def open_window_b():
    root.destroy()  # 關閉A視窗
    window_b_2.show_window_b()  # 顯示B視窗

# 創建主窗口A
root = tk.Tk()
root.title("A視窗")
root.geometry("300x200")

# 標題標籤
title_label = tk.Label(root, text="這是A視窗", font=("Arial", 14))
title_label.pack(pady=20)

# 切換到B視窗的按鈕
switch_button = tk.Button(root, text="切換到B視窗", font=("Arial", 12), command=open_window_b)
switch_button.pack(pady=20)

# 運行主循環
root.mainloop()