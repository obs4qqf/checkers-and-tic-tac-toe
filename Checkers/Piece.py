class Piece:

    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.alive = True

    def get_piece_jumping_position(self, captured_piece):
        row_diff = captured_piece.row - self.row
        col_diff = captured_piece.col - self.col
        opp_row = row_diff + captured_piece.row
        opp_col = col_diff + captured_piece.col
        return {'opp_row': opp_row, 'opp_col': opp_col}

    def capture_piece(self, captured_piece):
        self.row = self.get_piece_jumping_position(captured_piece)['opp_row']
        self.col = self.get_piece_jumping_position(captured_piece)['opp_col']
        captured_piece.alive = False

    def get_valid_moves(self):
        valid_moves = [[self.row + 1, self.col + 1],
                       [self.row - 1, self.col - 1],
                       [self.row + 1, self.col - 1],
                       [self.row - 1, self.col + 1]]
        return valid_moves
