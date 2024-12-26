# B視窗 - window_b.py
import tkinter as tk

def show_window_b():
    # 創建主窗口B
    root = tk.Tk()
    root.title("B視窗")
    root.geometry("300x200")

    # 標題標籤
    title_label = tk.Label(root, text="這是B視窗", font=("Arial", 14))
    title_label.pack(pady=20)

    # 運行主循環
    root.mainloop()