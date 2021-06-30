import random

spaces = {0: [" ", " ", " "], 1: [" ", " ", " "], 2: [" ", " ", " "]}  # Tracks board markers
player_win = False
bot_win = False
game_on = True
player_turn = True

print('Welcome to the Tic Tac Toe Match')
print('Beat the tic tac toe bot to win!')


def check_winner():
    '''
    Checks if a set of three squares on tic-tac-toe board has been completed/won
    '''
    global player_win
    global bot_win
    global game_on
    # matches records all possible winning combinations of filled squares, and also makes sure they aren't empty
    matches = [spaces[0][0] == spaces[0][1] == spaces[0][2] != " ",
               spaces[1][0] == spaces[1][1] == spaces[1][2] != " ",
               spaces[2][0] == spaces[2][1] == spaces[2][2] != " ",
               spaces[0][0] == spaces[1][0] == spaces[2][0] != " ",
               spaces[0][1] == spaces[1][1] == spaces[2][1] != " ",
               spaces[0][2] == spaces[1][2] == spaces[2][2] != " ",
               spaces[0][0] == spaces[1][1] == spaces[2][2] != " ",
               spaces[0][2] == spaces[1][1] == spaces[2][0] != " "]
    for match in matches:
        if match:  # checks if squares in match are same symbol
            if not player_turn:
                player_win = True
            else:
                bot_win = True
            game_on = False


def check_board_full():
    '''
    Checks if the tic-tac-toe board is full and if game is over
    :return: True/false if the board is full/not full
    '''
    board_full = True
    for row in spaces:
        for col in spaces:
            if spaces[row][col] == " ":
                board_full = False
    return board_full


def can_place_marker(row, col):
    '''
    Finds if tic-tac-toe square is empty
    :param row: The row number
    :param col: The column number
    :return: True/false if square is empty/filled
    '''
    if spaces[row][col] == 'X' or spaces[row][col] == 'O':
        return False
    else:
        return True


def bot_find_match(space1, space2, space3):
    '''
    Helps the bot find sets of two squares that could become winning tic-tac-toe rows
    :param space1: First square
    :param space2: Second square
    :param space3: Third square
    :return: True/false if there is a row where the player or the bot is about to win
    '''
    match1 = space1 == space2 != ' '
    match2 = space2 == space3 != ' '
    match3 = space1 == space3 != ' '
    return match1 or match2 or match3

# main game loop
while game_on and not player_win and not bot_win:
    print('-----------------------------------------')
    print('Tic Tac Toe Board:')
    print(f'|{spaces[0][0]}|{spaces[0][1]}|{spaces[0][2]}|\n|{spaces[1][0]}|{spaces[1][1]}|{spaces[1][2]}|\n|{spaces[2][0]}|{spaces[2][1]}|{spaces[2][2]}|')  # displays the tic-tac-toe board
    if player_turn:
        print('Your turn')
        row_num = input('Pick a row to place a marker: ')
        col_num = input('Pick a column to place a marker: ')

        while type(row_num) is not int or type(col_num) is not int:
            try:
                row_num = int(row_num)
                col_num = int(col_num)
            except ValueError:
                print('ERROR: Not valid coordinate. Please enter a new coordinate.')
                row_num = input('Pick a row to place a marker: ')
                col_num = input('Pick a column to place a marker: ')
            finally:
                if row_num < 1 or row_num > 3 or col_num < 1 or col_num > 3:
                    print('ERROR: Not valid coordinate entered.\n'
                          'Enter a new coordinates')
                    row_num = input('Pick a row to place a marker: ')
                    col_num = input('Pick a column to place a marker: ')
        if can_place_marker(row_num - 1, col_num - 1):
            spaces[row_num - 1][col_num - 1] = 'O'
            player_turn = False
        else:
            print('ERROR: Cannot place marker in occupied space.\n'
                  'Enter a new coordinate')
    else:
        print('Bot\'s turn')
        marker_placed = False  # ensures the bot only places one marker
        # new_matches records coordinates of squares together that result in victory
        new_matches = {1: [[0,0], [0,1], [0,2]],
                       2: [[1,0], [1,1], [1,2]],
                       3: [[2,0], [2,1], [2,2]],
                       4: [[0,0], [1,0], [2,0]],
                       5: [[0,1], [1,1], [2,1]],
                       6: [[0,2], [1,2], [2,2]],
                       7: [[0,0], [1,1], [2,2]],
                       8: [[0,2], [1,1], [2,0]]}

        # arrays below record sets of squares that result in player/bot victory
        player_can_win = []
        bot_can_win = []

        # checks for all possible ways the player or bot can win
        for match in new_matches:
            if bot_find_match(spaces[new_matches[match][0][0]][new_matches[match][0][1]], spaces[new_matches[match][1][0]][new_matches[match][1][1]], spaces[new_matches[match][2][0]][new_matches[match][2][1]]):
                for space in new_matches[match]:
                    if spaces[space[0]][space[1]] == 'X':
                        bot_can_win.append(new_matches[match])
                    elif spaces[space[0]][space[1]] == 'O':
                        player_can_win.append(new_matches[match])
        # bot win moves are prioritized over preventing player from winning
        if bot_can_win:
            for match in bot_can_win:
                for space in match:
                    if spaces[space[0]][space[1]] == ' ':
                        spaces[space[0]][space[1]] = 'X'
                        marker_placed = True
        # player win moves are prevented over random bot moves
        if player_can_win and not marker_placed:
            for match in player_can_win:
                for space in match:
                    if spaces[space[0]][space[1]] == ' ' and not marker_placed:
                        spaces[space[0]][space[1]] = 'X'
                        marker_placed = True
        while not marker_placed:
            rand_row = random.randint(0, 2)
            rand_col = random.randint(0, 2)
            if can_place_marker(rand_row, rand_col):
                spaces[rand_row][rand_col] = 'X'
                marker_placed = True
        player_turn = True
    check_winner()
    if check_board_full():
        game_on = False

if not game_on:
    print(f'|{spaces[0][0]}|{spaces[0][1]}|{spaces[0][2]}|\n|{spaces[1][0]}|{spaces[1][1]}|{spaces[1][2]}|\n|{spaces[2][0]}|{spaces[2][1]}|{spaces[2][2]}|')
    if not player_win and not bot_win:
        print('Game was a tie')
    if player_win and not bot_win:
        print('Player has won')
    if not player_win and bot_win:
        print('Bot has won')
    # user_replay = int(input('Play again? 1 for Yes and 2 for No: '))
    # if user_replay == 1:
    #     game_on = True


