
import tkinter as tk
from tkinter import font as tkFont

#初始化button_states
button_states = [False,False,False,False,False,False,False,False,False]

#button_states = [1,2,3,4,5,6,7,8,9]

print(bool(button_states))
current_player = "X" #X先手
def on_button_click(index):
   
   
    global current_player
    if current_player == "X":
    # 更新按鈕的狀態為已按下並將按現玩家更新到按鈕text 
        buttons[index].config(text=current_player)
        root.title("輪到玩家O決定位置")
        button_states[index] = current_player
        buttons[index].config(state="disabled")
        print(button_states)
    else: 
        buttons[index].config(text="O")
        root.title("輪到玩家X決定位置")
        button_states[index] = current_player
        buttons[index].config(state="disabled")
        print(button_states)
        #current_player = "X"
    # 如果所有按鈕都被按下且沒有分出勝負
    if all(button_states):
        root.title("平手")
        
    #每次按下按紐都會判定8種button_states 來確認是否有人獲勝
    if button_states[0] == button_states[1] == button_states[2] != False or\
       button_states[3] == button_states[4] == button_states[5] != False or\
       button_states[6] == button_states[7] == button_states[8] != False or\
       button_states[0] == button_states[3] == button_states[6] != False or\
       button_states[1] == button_states[4] == button_states[7] != False or\
       button_states[2] == button_states[5] == button_states[8] != False or\
       button_states[0] == button_states[4] == button_states[8] != False or\
       button_states[2] == button_states[4] == button_states[6] != False:   
        for btn in buttons: #當有人獲勝後將剩餘按鈕disable
            btn.config(state="disabled")   
            title = current_player+"  WIN!!!"   
        
   
        root.title(title)
     
    
    current_player = "O" if current_player == "X" else "X"

# 建立主視窗
root = tk.Tk()
root.title("井字遊戲 X先手")
root.resizable(0,0)
helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
# 建立顯示文字的標籤

# 建立按鈕
buttons = []
for i in range(9):
    btn = tk.Button(root, text=f"{i+1}",font=helv36, width=10, height=3, command=lambda i=i: on_button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# 運行主迴圈
root.mainloop()