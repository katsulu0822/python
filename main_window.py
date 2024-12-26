# -*- coding: utf-8 -*-
# A視窗 - main_window.py
import tkinter as tk
import window_login  # 匯入視窗B模組

def open_login():
    root.destroy()  # 關閉A視窗
    window_login.show_window()  # 顯示B視窗

# 創建主窗口A
root = tk.Tk()
root.title("Mystic-Match帳號管理系統")
root.geometry("400x200")

# 標題標籤
title_label = tk.Label(root, text="歡迎使用Mystic-Match請選擇註冊或登入帳號", font=("Arial", 14))
title_label.pack(pady=20)

# 切換到B視窗的按鈕
switch_button = tk.Button(root, text="登入", font=("Arial", 12), command=open_login)
switch_button.pack(pady=20)

# 運行主循環
root.mainloop()