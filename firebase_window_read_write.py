# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:03:41 2025

@author: user
"""

import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, db

# 初始化 Firebase
cred = credentials.Certificate("test2024-310f6-firebase-adminsdk-jszf0-987303813f.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://test2024-310f6-default-rtdb.firebaseio.com"})

# 写入 Firebase Realtime Database
def write_to_firebase():
    name = entry_name.get()
    email = entry_email.get()

    if not name or not email:
        messagebox.showerror("输入错误", "请输入有效的姓名和电子邮件！")
        return

    ref = db.reference('users')
    new_user_ref = ref.push({
        'name': name,
        'email': email
    })

    messagebox.showinfo("成功", f"数据已成功写入！用户 ID：{new_user_ref.key}")

# 从 Firebase Realtime Database 读取数据
def read_from_firebase():
    ref = db.reference('users')
    users_data = ref.get()

    if not users_data:
        messagebox.showinfo("数据", "没有找到任何用户数据！")
        return

    output = ""
    for user_id, user_info in users_data.items():
        output += f"用户 ID: {user_id}\n"
        output += f"姓名: {user_info['name']}\n"
        output += f"电子邮件: {user_info['email']}\n\n"
    
    text_output.delete(1.0, tk.END)  # 清空输出框
    text_output.insert(tk.END, output)

# 创建 GUI 窗口
root = tk.Tk()
root.title("Firebase 数据管理")

# 姓名输入框
label_name = tk.Label(root, text="姓名:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# 电子邮件输入框
label_email = tk.Label(root, text="电子邮件:")
label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# 写入按钮
button_write = tk.Button(root, text="写入数据", command=write_to_firebase)
button_write.grid(row=2, column=0, columnspan=2, pady=10)

# 读取按钮
button_read = tk.Button(root, text="读取数据", command=read_from_firebase)
button_read.grid(row=3, column=0, columnspan=2, pady=10)

# 显示输出区域
label_output = tk.Label(root, text="从 Firebase 获取的数据:")
label_output.grid(row=4, column=0, padx=10, pady=10)

text_output = tk.Text(root, height=10, width=40)
text_output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# 启动 GUI
root.mainloop()
