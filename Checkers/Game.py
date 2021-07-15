import Board


class Game:

    def __init__(self, symbol1, symbol2):
        self.board = Board.Board(symbol1, symbol2)
        self.player1_turn = True


    def game_won(self):
        return False

    def pick_piece(self, symbol):
        need_piece = True
        while need_piece:
            row = input('Pick pick a row with your piece (1-8): ')
            col = input('Pick pick a column with your piece (1-8): ')
            try:
                row = int(row)
                col = int(col)
                if 0 < row < 9 and 0 < col < 9:
                    row -= 1
                    col -= 1
                    if self.board.space_occupied(row, col):
                        if self.board.get_piece_at_space(row, col).symbol == symbol:
                            print('Piece selected!')
                            return self.board.get_piece_at_space(row, col)
                        else:
                            print('ERROR: Pick a space with your piece')
                    else:
                        print('ERROR: Pick a space with a marker')
                else:
                    print('ERROR: Pick a number in the appropriate ranges')
            except:
                print('ERROR: Pick a number')

    def move_piece(self, piece):
        need_move = True
        while need_move:
            row = input('Pick pick a row to move your piece to or to capture a piece (1-8): ')
            col = input('Pick pick a column to move your piece to or to capture a piece (1-8): ')
            try:
                row = int(row)
                col = int(col)
                row -= 1
                col -= 1
                valid_spaces = [[piece.row+1, piece.col+1],
                                [piece.row-1, piece.col-1],
                                [piece.row+1, piece.col-1],
                                [piece.row-1, piece.col+1]]
                if [row, col] in valid_spaces:
                    if not self.board.space_occupied(row, col):
                        piece.row = row
                        piece.col = col
                        need_move = False
                    else:
                        if self.board.get_piece_at_space(row, col).symbol != piece.symbol:
                            piece.capture_piece(self.board.get_piece_at_space(row, col))
                            need_move = False
                        else:
                            print('ERROR: Pick a space without your marker')
                else:
                    print('ERROR: Pick a number in the appropriate ranges')
            except:
                print('ERROR: Pick a number')

def main():
    symbol1 = 'O'
    symbol2 = 'X'
    game = Game(symbol1, symbol2)
    game.board.draw_board()
    print('Welcome to Checkers')
    while not game.game_won():
        if game.player1_turn:
            piece = game.pick_piece('O')
            game.move_piece(piece)
            game.board.draw_board()
        else:
            pass

if __name__ == "__main__":
    main()