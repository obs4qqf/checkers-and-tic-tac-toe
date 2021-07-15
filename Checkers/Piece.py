class Piece:

    def __init__(self, symbol, row, col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.alive = True
        # self.selected = False

    def capture_piece(self, piece):
        self.row = piece.row
        self.col = piece.col
        piece.alive = False
