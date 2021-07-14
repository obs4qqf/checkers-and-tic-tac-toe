import Board


class Game:

    def __init__(self, symbol1, symbol2):
        self.board = Board.Board(symbol1, symbol2)
        self.player1_turn = True


    def game_won(self):
        return False

    def pick_piece(self):
        need_piece = True
        while need_piece:
            row = input('Pick pick a row with your piece (1-8): ')
            col = input('Pick pick a column with your piece (1-8): ')
            try:
                row = int(row)
                col = int(col)
                if 0<row<9 and 0<col<9:
                    row -= 1
                    col -= 1
                    for piece in self.board.pieces:
                        if piece.row == row and piece.col == col:
                            piece.selected = True
                else:
                    print('ERROR: Pick a number in the appropriate ranges')
            except:
                print('ERROR: Pick a number')

def main():
    game = Game('O', 'X')
    game.board.draw_board()
    print('Welcome to Checkers')
    while not game.game_won():
        if game.player1_turn:
            game.pick_piece()
        else:
            pass

if __name__ == "__main__":
    main()