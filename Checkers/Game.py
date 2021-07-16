import Board


class Game:
    """
    Defines basic board game objects and general checkers game methods.
    """

    def __init__(self, symbol1, symbol2):
        """
        Creates a Game object to begin checkers game
        :param symbol1: Player 1's marker symbol as a string
        :param symbol2: Player 2's marker symbol as a string
        """
        self.board = Board.Board(symbol1, symbol2)
        self.player1_turn = True


    def game_won(self):
        return False

    def pick_piece(self, symbol):
        """
        Allows the player to pick a piece and checks if that piece is valid to pick
        :param symbol: The current player's piece symbol as a string
        :return: The chosen piece as a Piece object
        """
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
                        piece = self.board.get_piece_at_space(row, col)
                        if piece.symbol == symbol:
                            if self.board.can_move_piece(piece):
                                print('Piece selected!')
                                return self.board.get_piece_at_space(row, col)
                            else:
                                print('ERROR: Pick a piece that can be moved')
                        else:
                            print('ERROR: Pick a space with your piece')
                    else:
                        print('ERROR: Pick a space with a marker')
                else:
                    print('ERROR: Pick a number in the appropriate ranges')
            except:
                print('ERROR: Pick a number')

    def move_piece(self, piece):
        """
        Moves the selected piece to a valid nearby location that the player defines
        :param piece: The piece selected previously as a Piece object
        """
        need_move = True
        while need_move:
            row = input('Pick pick a row to move your piece to or to capture a piece (1-8): ')
            col = input('Pick pick a column to move your piece to or to capture a piece (1-8): ')
            try:
                row = int(row)
                col = int(col)
                row -= 1
                col -= 1
                if [row, col] in piece.get_valid_moves():
                    if not self.board.space_occupied(row, col):
                        piece.row = row
                        piece.col = col
                        need_move = False
                    else:
                        nearby_piece = self.board.get_piece_at_space(row, col)
                        if nearby_piece.symbol != piece.symbol:
                            if self.board.can_capture_piece(piece, nearby_piece):
                                piece.capture_piece(nearby_piece)
                                need_move = False
                            else:
                                print('ERROR: The piece you have selected cannot be captured')
                        else:
                            print('ERROR: Pick a space without your marker')
                else:
                    print('ERROR: Pick a valid space nearby your piece')
            except:
                print('ERROR: Pick a number')

def main():
    """
    Defines the main game loop
    """
    symbol1 = 'O'
    symbol2 = 'X'
    game = Game(symbol1, symbol2)
    game.board.draw_board()
    print('Welcome to Checkers')
    while not game.game_won():
        if game.player1_turn:
            print('Player', symbol1, 'turn')
            piece = game.pick_piece('O')
            game.move_piece(piece)
            game.board.draw_board()
            game.player1_turn = False
        else:
            # pass
            print('Player', symbol2, 'turn')
            piece = game.pick_piece('X')
            game.move_piece(piece)
            game.board.draw_board()
            game.player1_turn = True

if __name__ == "__main__":
    main()