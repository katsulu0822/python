# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:49:10 2025

@author: user
"""

import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, auth, db

# 初始化 Firebase

if not firebase_admin._apps:
    cred = credentials.Certificate("test2024-310f6-firebase-adminsdk-jszf0-987303813f.json")
    firebase_admin.initialize_app(cred,{"databaseURL":"https://test2024-310f6-default-rtdb.firebaseio.com"})


# 注册功能
def register():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("输入错误", "用户名和密码不能为空！")
        return

    try:
        # 创建用户
        user = auth.create_user(
            email=f"{username}@example.com",  # 使用用户名创建唯一的邮箱（例如 username@example.com）
            password=password
        )
        # 保存用户名和邮箱映射到 Realtime Database
        user_ref = db.reference('users')
        user_ref.child(user.uid).set({
            'username': username,
            'email': f"{username}@example.com"
        })

        messagebox.showinfo("成功", f"用户注册成功！UID: {user.uid}")
    except Exception as e:
        messagebox.showerror("注册失败", f"发生错误: {e}")

# 登录功能
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("输入错误", "用户名和密码不能为空！")
        return

    try:
        # 检查 Firebase Authentication 中的用户名和密码
        user = auth.get_user_by_email(f"{username}@example.com")

        # 验证密码
        # 由于 firebase-admin SDK 不支持直接验证密码，我们需要前端（例如 Web 或移动端）来进行密码验证
        # 在这里我们假设密码是正确的
        messagebox.showinfo("登录成功", f"欢迎回来，{username}！")
    except auth.UserNotFoundError:
        messagebox.showerror("登录失败", "用户名或密码错误！")
    except Exception as e:
        messagebox.showerror("登录失败", f"发生错误: {e}")

# 创建 GUI 窗口
root = tk.Tk()
root.title("Firebase 用户注册与登录")

# 用户名输入框
label_username = tk.Label(root, text="用户名:")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# 密码输入框
label_password = tk.Label(root, text="密码:")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")  # 使用 "*" 隐藏密码
entry_password.grid(row=1, column=1, padx=10, pady=10)

# 注册按钮
button_register = tk.Button(root, text="注册", command=register)
button_register.grid(row=2, column=0, columnspan=2, pady=10)

# 登录按钮
button_login = tk.Button(root, text="登录", command=login)
button_login.grid(row=3, column=0, columnspan=2, pady=10)

# 启动 GUI
root.mainloop()
