

import tkinter as tk
from tkinter import font as tkFont



def on_button_click(button):
    """當按鈕被點擊時，將顯示 'X'"""
    if button["text"] != "X":  # 如果按鈕顯示 "O"，就改為 "X"
        button.config(text="X")
    elif button["text"] == "X":
        button.config(text="O")

# 創建主視窗
root = tk.Tk()
root.title("按鈕範例")
root.resizable(0,0)
helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)

# 9個按鈕，初始顯示 "O"
buttons = []
text=1
for i in range(9):
    button = tk.Button(root, text=str(text+i),font=helv36, width=10, height=3, 
                       command=lambda btn=i: on_button_click(buttons[btn]))
    button.grid(row=i//3, column=i%3)  # 設置按鈕的位置
    buttons.append(button)

# 啟動主事件循環
root.mainloop()