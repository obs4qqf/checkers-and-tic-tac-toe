import Piece


class Board:

    def __init__(self, symbol1, symbol2):
        self.pieces = [Piece.Piece(symbol1, 0, 1), Piece.Piece(symbol1, 0, 3), Piece.Piece(symbol1, 0, 5), Piece.Piece(symbol1, 0, 7),
                       Piece.Piece(symbol1, 1, 0), Piece.Piece(symbol1, 1, 2), Piece.Piece(symbol1, 1, 4), Piece.Piece(symbol1, 1, 6),
                       Piece.Piece(symbol1, 2, 1), Piece.Piece(symbol1, 2, 3), Piece.Piece(symbol1, 2, 5), Piece.Piece(symbol1, 2, 7),
                       Piece.Piece(symbol2, 5, 0), Piece.Piece(symbol2, 5, 2), Piece.Piece(symbol2, 5, 4), Piece.Piece(symbol2, 5, 6),
                       Piece.Piece(symbol2, 6, 1), Piece.Piece(symbol2, 6, 3), Piece.Piece(symbol2, 6, 5), Piece.Piece(symbol2, 6, 7),
                       Piece.Piece(symbol2, 7, 0), Piece.Piece(symbol2, 7, 2), Piece.Piece(symbol2, 7, 4), Piece.Piece(symbol2, 7, 6)]

    def draw_board(self):
        board = [[' ' for x in range(8)] for x in range(8)]
        for piece in self.pieces:
            if piece.alive:
                board[piece.row][piece.col] = piece.symbol
        for row in board:
            print(f'{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}|{row[6]}|{row[7]}')

    def space_occupied(self, row, col):
        piece_present = False
        for piece in self.pieces:
            if piece.row == row and piece.col == col and piece.alive:
                piece_present = True
        return piece_present

    def get_piece_at_space(self, row, col):
        for piece in self.pieces:
            if piece.row == row and piece.col == col and piece.alive:
                return piece

    def can_move_piece(self, piece):
        moves_available = True
        for moves in piece.valid_moves:
            new_row = moves[0]
            new_col = moves[1]
            if 0 < new_row < 9 and 0 < new_col < 9:
                if self.space_occupied(new_row, new_col):
                    moves_available = False
        return moves_available

    def can_capture_piece(self):
        pass

# def main():
#     Board('O','X').draw_board()
#
#
# if __name__ == "__main__":
#     main()
