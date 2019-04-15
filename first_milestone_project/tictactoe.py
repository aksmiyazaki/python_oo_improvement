import os
game_board = [['', '', ''],
                ['', '', ''],
                ['', '', '']]


def print_board(board):
    for row in board:
        str_to_print = ""
        for idx, cel in enumerate(row):
            if cel == 'X':
                str_to_print += 'X'
            elif cel == 'O':
                str_to_print += 'O'
            else:
                str_to_print += '_'

            if idx != 2:
                str_to_print += '|'
        print(str_to_print)

def check_game_win(board, check_pl):
    # Check lines
    for i in range(0,3):
        win = True
        for j in range(0,3):
            if board[i][j] != check_pl:
                win = False
        if win:
            return True

    # check columns
    for i in range(0,3):
        win = True
        for j in range(0,3):
            if board[j][i] != check_pl:
                win = False
        if win:
            return True

    # Check diag
    if board[0][0] == check_pl and board[1][1] == check_pl and board[2][2] == check_pl:
        return True

    if board[0][2] == check_pl and board[1][1] == check_pl and board[2][0] == check_pl:
        return True

    return False

def run_the_game():
    running_game = True
    turn = "Player 1"
    while(running_game):
        print("The current state of the game is:")
        print_board(game_board)
        get_input = True
        while get_input:
            user_input = input("Select the cell (1-9 from left to right, bottom to top)")
            if user_input >= 1 and user_input <= 9:
                get_input = False



waiting_input = True
players = {'Player 1': '','Player 2':''}
while(waiting_input):
    os.system('cls')
    res = input("Hey Player one, do you want to be 'X' or 'O'?").strip().upper()
    if res in ['X', 'O']:
        waiting_input = False
        players['Player 1'] = res
        players['Player 2'] = list(filter(lambda x: x != res, ['X', 'O']))[0]
    else:
        input("Invalid input, press any key to continue.")

os.system('cls')
print(f"All Set!")
for key, value in players.items():
    print(f"{key} Will be {value}")
