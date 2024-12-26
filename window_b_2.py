# B視窗 - window_b.py
import tkinter as tk
from tkinter import messagebox

# 模擬正確的帳號密碼
correct_username = "admin"
correct_password = "1234"

def login_correct(username, password):
    if username == correct_username and password == correct_password:
        messagebox.showinfo("登入成功", "歡迎使用！")
    else:
        messagebox.showerror("登入失敗", "帳號或密碼錯誤！")

def show_window_b():
    # 創建主窗口B
    root = tk.Tk()
    root.title("B視窗")
    root.geometry("300x200")

    # 標題標籤
    title_label = tk.Label(root, text="請登入", font=("Arial", 14))
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

    # 登入按鈕
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        login_correct(username, password)

    login_button = tk.Button(root, text="登入", command=handle_login)
    login_button.pack(pady=10)

    # 運行主循環
    root.mainloop()
