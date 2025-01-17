# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:39:20 2025

@author: user
"""

import random

# 顯示遊戲板
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# 檢查是否有玩家獲勝
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 橫向
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 垂直
        [0, 4, 8], [2, 4, 6]  # 斜向
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# 檢查遊戲是否結束
def is_board_full(board):
    return all([spot == "\033[43mO\033[0m" or spot == "\033[46mX\033[0m" for spot in board])

# 電腦選擇位置
def computer_move(board):
    empty_spots = [i for i, spot in enumerate(board) if spot != "\033[43mO\033[0m" and spot != "\033[46mX\033[0m"]
    return random.choice(empty_spots)  # 隨機選擇一個空格

# 主遊戲邏輯
def play_game():
    # 初始化遊戲板
    board = []
    for i in range(9):
        board.append("\033[42m"+str(i+1)+"\033[0m")  # 顯示1-9的格子
    current_player = "\033[46mX\033[0m"  # 先手玩家為 "X"（假設是電腦）
    
    while True:
        print_board(board)  # 顯示當前遊戲板
        
        if current_player == "\033[46mX\033[0m":  # 電腦的回合
            print("電腦正在選擇...")
            move = computer_move(board)
            print(f"電腦選擇了位置 {move + 1}")
        else:  # 玩家回合
            try:
                move = int(input(f"玩家 {current_player} 請選擇位置（1-9）輸入99可強制結束：")) - 1
                if move == 98:
                    print("強制結束")  # 強制結束遊戲
                    break
                elif move < 0 or move > 8:
                    print("位置超出範圍，請重新選擇。")
                    continue
                elif board[move] == "\033[43mO\033[0m" or board[move] == "\033[46mX\033[0m":
                    print("這個位置已經被佔用了，請重新選擇。")
                    continue
            except ValueError:
                print("請輸入有效的數字。")
                continue
        
        board[move] = current_player  # 玩家或電腦下棋

        # 檢查是否有玩家獲勝
        if check_winner(board, current_player):
            print_board(board)
            print(f"玩家 {current_player} 獲勝！")
            break

        # 檢查是否平局
        if is_board_full(board):
            print_board(board)
            print("遊戲結束，平局！")
            break

        # 換玩家
        current_player = "\033[43mO\033[0m" if current_player == "\033[46mX\033[0m" else "\033[46mX\033[0m"

# 開始遊戲
if __name__ == "__main__":
    play_game()
