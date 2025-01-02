# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:09:24 2025

@author: user
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from transformers import pipeline
from PIL import Image, ImageTk
import requests

# 初始化模型和 pipeline
pipe = pipeline("image-to-text", model="microsoft/trocr-base-handwritten")

# 建立主視窗
root = tk.Tk()
root.title("手寫文字識別")
root.geometry("600x500")

# 顯示圖片的 Label
image_label = tk.Label(root, text="請選擇圖片", width=50, height=15, relief="solid")
image_label.pack(pady=20)

# 顯示識別結果的 Label
result_label = tk.Label(root, text="識別結果將顯示在這裡", wraplength=500, justify="left", font=("Arial", 12))
result_label.pack(pady=10)

# 處理圖片並識別文字的函數
def recognize_text(image_path):
    try:
        # 載入圖片
        image = Image.open(image_path).convert("RGB")

        # 使用 pipeline 進行手寫文字識別
        predicted_text = pipe(image)[0]['generated_text']

        # 顯示識別結果
        result_label.config(text="識別結果: \n" + predicted_text)

    except Exception as e:
        messagebox.showerror("錯誤", f"圖片處理時出現錯誤: {e}")

# 上傳圖片的函數
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.webp")])
    if file_path:
        # 顯示圖片
        img = Image.open(file_path)
        img.thumbnail((200, 200))  # 調整縮圖大小
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk, text="")  # 顯示圖片，並移除預設文字
        image_label.image = img_tk

        # 開始識別圖片中文字
        recognize_text(file_path)

# 按鈕：選擇圖片
upload_button = tk.Button(root, text="上傳圖片", command=upload_image, width=20, height=2)
upload_button.pack()

# 主循環
root.mainloop()
