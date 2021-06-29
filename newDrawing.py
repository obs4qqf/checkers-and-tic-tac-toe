
spaces = {0: [" ", " ", " "], 1: [" ", " ", " "], 2: [" ", " ", " "]}
playerWin = False
botWin = False
gameOn = True
playerTurn = True

print('Welcome to the Tic Tac Toe Match')
print('Beat the tic tac toe bot to win!')

def check_winner():
    global playerWin
    global botWin
    global gameOn
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
            if not playerTurn:
                playerWin = True
            else:
                botWin = True
            gameOn = False

while gameOn and not playerWin and not botWin:
    print('Tic Tac Toe Board:')
    print(f'|{spaces[0][0]}|{spaces[0][1]}|{spaces[0][2]}|\n|{spaces[1][0]}|{spaces[1][1]}|{spaces[1][2]}|\n|{spaces[2][0]}|{spaces[2][1]}|{spaces[2][2]}|')
    if playerTurn:
        rowNum = int(input('Pick a row to place a marker: '))
        colNum = int(input('Pick a column to place a marker: '))
        spaces[rowNum - 1][colNum - 1] = "O"
        playerTurn = False
    else:
        rowNum = int(input('Pick a row to place a marker: '))
        colNum = int(input('Pick a column to place a marker: '))
        spaces[rowNum - 1][colNum - 1] = "X"
        playerTurn = True
    check_winner()

if not gameOn and not playerWin and not botWin:
    print('Game was a tie')

if not gameOn and playerWin and not botWin:
    print('Player has won')

if not gameOn and not playerWin and botWin:
    print('Bot has won')


