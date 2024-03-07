import random as r


def ph():
    return "Sorry, this game is currently indev"


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def player_move(board, player):
    while True:
        print_board(board)
        row = int(input(player + ", enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = player
            break
        else:
            print("Cell already taken. Try again.")


def computer_move(board, player):
    print(player, "'s turn:")
    while True:
        row = r.randint(0, 2)
        col = r.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = player
            break


def rerun():
    print("Rerun?")
    a = input("+/-:")
    if a == "+":
        main()


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    t = 0

    game_mode = input("Select game mode (1 for single player, 2 for two players): ")

    while t == 0:
        if game_mode == "1" and current_player == "O":
            computer_move(board, current_player)
        elif game_mode == "2" or current_player == "X":
            player_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(current_player, " wins!")
            t = 1
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            t = 1
        else:
            current_player = "O" if current_player == "X" else "X"
    rerun()
