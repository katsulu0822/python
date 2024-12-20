# 井字遊戲

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
    return all([spot != " " for spot in board])

# 主遊戲邏輯
def play_game():
    board = [" "] * 9  # 初始化井字板
    current_player = "X"  # 先手玩家為 "X"

    while True:
        print_board(board)  # 顯示當前遊戲板
        move = int(input(f"玩家 {current_player} 請選擇位置（1-9）：")) - 1

        # 確保選擇的格子有效且尚未被佔用
        if board[move] != " ":
            print("這個位置已經被佔用了，請重新選擇。")
            continue

        board[move] = current_player  # 玩家在指定位置放置標記

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
        current_player = "O" if current_player == "X" else "X"

# 開始遊戲
if __name__ == "__main__":
    play_game()