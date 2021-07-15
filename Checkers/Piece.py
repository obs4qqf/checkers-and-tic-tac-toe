class Piece:

    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.alive = True

    def capture_piece(self, piece):
        self.row = piece.row
        self.col = piece.col
        piece.alive = False

    def get_valid_moves(self):
        valid_moves = [[self.row + 1, self.col + 1],
                       [self.row - 1, self.col - 1],
                       [self.row + 1, self.col - 1],
                       [self.row - 1, self.col + 1]]
        return valid_moves
