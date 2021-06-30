import random

spaces = {0: [" ", " ", " "], 1: [" ", " ", " "], 2: [" ", " ", " "]}
player_win = False
bot_win = False
game_on = True
player_turn = True

print('Welcome to the Tic Tac Toe Match')
print('Beat the tic tac toe bot to win!')


def check_winner():
    global player_win
    global bot_win
    global game_on
    matches = [spaces[0][0] == spaces[0][1] == spaces[0][2] != " ",
               spaces[1][0] == spaces[1][1] == spaces[1][2] != " ",
               spaces[2][0] == spaces[2][1] == spaces[2][2] != " ",
               spaces[0][0] == spaces[1][0] == spaces[2][0] != " ",
               spaces[0][1] == spaces[1][1] == spaces[2][1] != " ",
               spaces[0][2] == spaces[1][2] == spaces[2][2] != " ",
               spaces[0][0] == spaces[1][1] == spaces[2][2] != " ",
               spaces[0][2] == spaces[1][1] == spaces[2][0] != " "]
    for match in matches:
        if match:
            if not player_turn:
                player_win = True
            else:
                bot_win = True
            game_on = False


def check_board_full():
    board_full = True
    for row in spaces:
        for col in spaces:
            if spaces[row][col] == " ":
                board_full = False
    return board_full


def can_place_marker(row, col):
    if spaces[row][col] == 'X' or spaces[row][col] == 'O':
        return False
    else:
        return True

while game_on and not player_win and not bot_win:
    print('-----------------------------------------')
    print('Tic Tac Toe Board:')
    print(f'|{spaces[0][0]}|{spaces[0][1]}|{spaces[0][2]}|\n|{spaces[1][0]}|{spaces[1][1]}|{spaces[1][2]}|\n|{spaces[2][0]}|{spaces[2][1]}|{spaces[2][2]}|')
    if player_turn:
        print('Your turn')
        row_num = int(input('Pick a row to place a marker: '))
        col_num = int(input('Pick a column to place a marker: '))
        if 0 < row_num < 4 and 0 < col_num < 4:
            if can_place_marker(row_num - 1, col_num - 1):
                spaces[row_num - 1][col_num - 1] = 'O'
                player_turn = False
            else:
                print('ERROR: Cannot place marker in occupied space.\n'
                      'Enter a new coordinate')
        else:
            print('ERROR: Not valid coordinate entered.\n'
                  'Enter a new coordinate')
    else:
        print('Bot\'s turn')
        marker_placed = False
        # row_num = int(input('Pick a row to place a marker: '))
        # col_num = int(input('Pick a column to place a marker: '))
        # if can_place_marker(row_num - 1, col_num - 1):
        #     spaces[row_num - 1][col_num - 1] = 'X'
        #     player_turn = True
        # else:
        #     print('Cannot place marker in occupied space.\n'
        #           'Enter a new coordinate')
        new_matches = [[spaces[0][0], spaces[0][1], spaces[0][2]],
                       [spaces[1][0], spaces[1][1], spaces[1][2]],
                       [spaces[2][0], spaces[2][1], spaces[2][2]],
                       [spaces[0][0], spaces[1][0], spaces[2][0]],
                       [spaces[0][1], spaces[1][1], spaces[2][1]],
                       [spaces[0][2], spaces[1][2], spaces[2][2]],
                       [spaces[0][0], spaces[1][1], spaces[2][2]],
                       [spaces[0][2], spaces[1][1], spaces[2][0]]]

        bot_moves = [[0,2],
                     [0,0],
                     [1,2],
                     [1,0],
                     [2,2],
                     [2,0],
                     [2,0],
                     [0,0],
                     [2,1],
                     [0,1],
                     [2,2],
                     [0,2],
                     [2,2],
                     [0,0],
                     [2,0],
                     [0,2]]

        for match in new_matches:
            if match[0] == match[1] != ' ' or match[1] == match[2] != ' ' or match[0] == match[2] != ' ':
                for space in match:
                    if space == ' ':
                        space = 'X'
                        marker_placed = True
                        print('1')
                        print(space)
        while not marker_placed:
            rand_row = random.randint(0, 2)
            rand_col = random.randint(0, 2)
            if can_place_marker(rand_row, rand_col):
                spaces[rand_row][rand_col] = 'X'
                marker_placed = True
            print('2')
        player_turn = True



    check_winner()
    if check_board_full():
        game_on = False

if not game_on and not player_win and not bot_win:
    print('Game was a tie')

if not game_on and player_win and not bot_win:
    print('Player has won')

if not game_on and not player_win and bot_win:
    print('Bot has won')


