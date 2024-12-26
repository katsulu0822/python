# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:49:40 2024

@author: user
"""

# B視窗 - window_b.py
import tkinter as tk
import firebase_admin
from firebase_admin import credentials, db

# 初始化Firebase連線
cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")  # 替換為你的Firebase Admin SDK路徑
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-name.firebaseio.com/'  # 替換為你的Firebase資料庫URL
})

def register_account(username, password):
    ref = db.reference("users")  # 指向"users"節點
    ref.push({"username": username, "password": password})  # 儲存使用者資料
    print("註冊成功！")

def show_window_b():
    # 創建主窗口B
    root = tk.Tk()
    root.title("註冊帳號")
    root.geometry("300x300")

    # 標題標籤
    title_label = tk.Label(root, text="請註冊帳號", font=("Arial", 14))
    title_label.pack(pady=10)

    # 使用者名稱輸入框
    username_label = tk.Label(root, text="使用者名稱：", font=("Arial", 12))
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    # 密碼輸入框
    password_label = tk.Label(root, text="密碼：", font=("Arial", 12))
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # 註冊按鈕
    def handle_register():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            register_account(username, password)
            tk.messagebox.showinfo("成功", "註冊成功！")
            root.destroy()
        else:
            tk.messagebox.showerror("錯誤", "請輸入使用者名稱和密碼！")

    register_button = tk.Button(root, text="註冊", command=handle_register)
    register_button.pack(pady=10)

    # 運行主循環
    root.mainloop()
