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
        if self.board.check_board_empty():
            return True
        moves_available_1 = False
        moves_available_2 = False
        for piece in self.board.pieces:
            if self.board.can_move_piece(piece) and piece.alive and piece.player == 1:
                moves_available_1 = True
        for piece in self.board.pieces:
            if self.board.can_move_piece(piece) and piece.alive and piece.player == 2:
                moves_available_2 = True
        return not (moves_available_1 and moves_available_2)

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
                    row -= 1  # Converts row/column number from 1-8 scale to be on 0-7 scale
                    col -= 1
                    if self.board.space_occupied(row, col):
                        piece = self.board.get_piece_at_space(row, col)
                        if piece.symbol == symbol:
                            if self.board.can_move_piece(piece):  # Checks if piece can move/capture another piece
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
                row -= 1  # Converts row/column number from 1-8 scale to be on 0-7 scale
                col -= 1
                if [row, col] in piece.get_valid_moves():  # Checks if space chosen is diagonally located to piece
                    if not self.board.space_occupied(row, col):
                        piece.row = row
                        piece.col = col
                        need_move = False
                    else:
                        nearby_piece = self.board.get_piece_at_space(row, col)
                        if nearby_piece.symbol != piece.symbol:  # Checks if space is occupied by opponent's piece
                            if self.board.can_capture_piece(piece, nearby_piece):
                                piece.capture_piece(nearby_piece)
                                need_move = False
                            else:
                                print('ERROR: The piece you have selected cannot be captured')
                        else:  # This is entered if space is occupied by player's own marker
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
    # game.board.init_piece_positions(symbol1, symbol2)  # used for debugging purposes to pick chess piece positions
    # game.player1_turn = True  # used for debugging purposes
    game.board.draw_board()
    print('Welcome to Checkers')
    while not game.game_won():
        if game.player1_turn:
            print('Player', symbol1, 'turn')
            piece = game.pick_piece('O')
            game.move_piece(piece)
            game.board.make_piece_king(piece)
            game.board.draw_board()
            if game.game_won():
                break
            game.player1_turn = False
        else:
            # pass
            print('Player', symbol2, 'turn')
            piece = game.pick_piece('X')
            game.move_piece(piece)
            game.board.make_piece_king(piece)
            game.board.draw_board()
            if game.game_won():
                break
            game.player1_turn = True
    if game.player1_turn:
        print('Player 1 has won')
    else:
        print('Player 2 has won')

if __name__ == "__main__":
    main()