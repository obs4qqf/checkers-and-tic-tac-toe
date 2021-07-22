class Piece:
    """
    Records the location, activity, and player assigned to a checkers marker
    """

    def __init__(self, symbol, row, col, player, king):
        """
        Creates a checkers marker
        :param symbol: The marker symbol as a string
        :param row: The row of the square as an integer from 0-7 inclusive
        :param col: The column of the square as an integer from 0-7 inclusive
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.alive = True
        self.player = player
        self.king = king

    def get_piece_jumping_position(self, captured_piece):
        """
        Retrieves the position a piece will end up in when it jumps/captures another piece
        :param captured_piece: The piece to be captured
        :return: The row and column number of the position as integers in a dictionary
        """
        row_diff = captured_piece.row - self.row  # Compares the row/column numbers of the two pieces
        col_diff = captured_piece.col - self.col
        opp_row = row_diff + captured_piece.row
        opp_col = col_diff + captured_piece.col
        return {'opp_row': opp_row, 'opp_col': opp_col}

    def capture_piece(self, captured_piece):
        """
        Moves jumping piece and removes captured piece on the board
        :param captured_piece:
        :return:
        """
        self.row = self.get_piece_jumping_position(captured_piece)['opp_row']
        self.col = self.get_piece_jumping_position(captured_piece)['opp_col']
        captured_piece.alive = False

    def get_valid_moves(self):
        """
        Checks for the positions of immediately-located squares on the diagonals nearby the current piece
        :return: The coordinates of squares a piece may move to in a nested array object
        """
        if self.king:
            valid_moves = [[self.row + 1, self.col + 1],
                           [self.row + 1, self.col - 1],
                           [self.row - 1, self.col - 1],
                           [self.row - 1, self.col + 1]]
        else:
            if self.player == 1:
                valid_moves = [[self.row + 1, self.col + 1],
                               [self.row + 1, self.col - 1]]
            else:
                valid_moves = [[self.row - 1, self.col - 1],
                               [self.row - 1, self.col + 1]]
        return valid_moves
