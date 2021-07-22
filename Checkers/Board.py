import Piece

class Board:
    """
    Holds data and methods for all Piece objects in board game
    """

    def __init__(self, symbol1, symbol2):
        """
        Creates a Board object with various pieces and assigns them to locations on the board
        :param symbol1: Player 1's marker symbol as a string
        :param symbol2: Player 2's marker symbol as a string
        """
        # Inactive pieces remain in the pieces array, but have an attribute of alive = False
        self.pieces = [Piece.Piece(symbol1, 0, 1, 1, False), Piece.Piece(symbol1, 0, 3, 1, False),
                       Piece.Piece(symbol1, 0, 5, 1, False), Piece.Piece(symbol1, 0, 7, 1, False),
                       Piece.Piece(symbol1, 1, 0, 1, False), Piece.Piece(symbol1, 1, 2, 1, False),
                       Piece.Piece(symbol1, 1, 4, 1, False), Piece.Piece(symbol1, 1, 6, 1, False),
                       Piece.Piece(symbol1, 2, 1, 1, False), Piece.Piece(symbol1, 2, 3, 1, False),
                       Piece.Piece(symbol1, 2, 5, 1, False), Piece.Piece(symbol1, 2, 7, 1, False),
                       Piece.Piece(symbol2, 5, 0, 2, False), Piece.Piece(symbol2, 5, 2, 2, False),
                       Piece.Piece(symbol2, 5, 4, 2, False), Piece.Piece(symbol2, 5, 6, 2, False),
                       Piece.Piece(symbol2, 6, 1, 2, False), Piece.Piece(symbol2, 6, 3, 2, False),
                       Piece.Piece(symbol2, 6, 5, 2, False), Piece.Piece(symbol2, 6, 7, 2, False),
                       Piece.Piece(symbol2, 7, 0, 2, False), Piece.Piece(symbol2, 7, 2, 2, False),
                       Piece.Piece(symbol2, 7, 4, 2, False), Piece.Piece(symbol2, 7, 6, 2, False)]

    def draw_board(self):
        """
        Prints the board based on the positions of each Piece object in the board
        """
        rowLabel = 1
        board = [[' ' for x in range(8)] for x in range(8)]  # An empty board is drawn
        for piece in self.pieces:
            if piece.alive:
                board[piece.row][piece.col] = piece.symbol
        print('  1|2|3|4|5|6|7|8')
        for row in board:
            print(f'{rowLabel} {row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}|{row[6]}|{row[7]}')
            rowLabel += 1
        print('  1|2|3|4|5|6|7|8')

    def space_occupied(self, row, col):
        """
        Checks whether a space on the board has a piece assigned to it or not
        :param row: The row of the space as an integer from 0-7 inclusive
        :param col: The column of the space as an integer from 0-7 inclusive
        :return: Whether the space is occupied as a boolean
        """
        piece_present = False
        for piece in self.pieces:
            if piece.row == row and piece.col == col and piece.alive:  # Only alive pieces are checked
                piece_present = True
        return piece_present

    def get_piece_at_space(self, row, col):
        """
        Finds and retrieves the piece at a certain square
        :param row: The row of the square as an integer from 0-7 inclusive
        :param col: The column of the square as an integer from 0-7 inclusive
        :return: The piece as a Piece object
        """
        for piece in self.pieces:
            if piece.row == row and piece.col == col and piece.alive:
                return piece

    def can_move_piece(self, piece):
        """
        Checks whether a piece can be moved to a nearby location
        Also looks to see if any nearby pieces can be captured (and cause the current piece to move)
        :param piece: The Piece object that is being moved
        :return: A boolean defining whether the piece can be moved
        """
        moves_available = False
        for move in piece.get_valid_moves():
            new_row = move[0]  # Records a potential row/column to move to
            new_col = move[1]
            if -1 < new_row <= 8 and -1 < new_col < 8:  # Checks if row/column is on the board
                if self.space_occupied(new_row, new_col):
                    nearby_piece = self.get_piece_at_space(new_row, new_col)
                    if nearby_piece.player != piece.player:
                        # This checks if the opponent's piece (that is nearby the player's piece) can be captured
                        moves_available = moves_available or self.can_capture_piece(piece, nearby_piece)
                else:  # This is entered if the space is unoccupied
                    moves_available = moves_available or True
        return moves_available

    def can_capture_piece(self, piece1, piece2):
        """
        Checks to see if a piece can be captured by another piece
        :param piece1: The piece attempting to capture
        :param piece2: The piece that is being captured
        :return: A boolean representing whether a piece can be captured
        """
        opp_row = piece1.get_piece_jumping_position(piece2)['opp_row']
        opp_col = piece1.get_piece_jumping_position(piece2)['opp_col']
        if -1 < opp_row <= 8 and -1 < opp_col < 8:  # Checks if the position after jumping is on the board
            return not self.space_occupied(opp_row, opp_col)
        else:
            return False

    def player_has_no_pieces(self):
        player1 = True
        player2 = True
        for piece in self.pieces:
            if piece.alive and piece.player == 1:
                player1 = False
        for piece in self.pieces:
            if piece.alive and piece.player == 2:
                player2 = False
        return player1 and player2

    def make_piece_king(self, piece):
        if piece.player == 1 and piece.row == 7:
            piece.king = True
            piece.symbol = '@'
        if piece.player == 2 and piece.row == 0:
            piece.king = True
            piece.symbol = '%'

    def get_pieces_amount(self, player):
        count = 0
        for piece in self.pieces:
            if piece.alive and piece.player == player:
                count += 1
        return count

    def get_available_moves(self, piece):
        moves_available = []
        for move in piece.get_valid_moves():
            new_row = move[0]
            new_col = move[1]
            if -1 < new_row <= 8 and -1 < new_col < 8:
                if self.space_occupied(new_row, new_col):
                    nearby_piece = self.get_piece_at_space(new_row, new_col)
                    if nearby_piece.player != piece.player and self.can_capture_piece(piece, nearby_piece):
                        row = piece.get_piece_jumping_position(nearby_piece)['opp_row']
                        col = piece.get_piece_jumping_position(nearby_piece)['opp_col']
                        moves_available.append([row, col, nearby_piece])
                else:  # This is entered if the space is unoccupied
                    moves_available.append([new_row, new_col, None])
        return moves_available

    def init_piece_positions(self, symbol1, symbol2):
        """
        Places pieces in specific positions for testing purposes
        :param symbol1: Player 1's symbol
        :param symbol2: Player 2's symbol
        :return:
        """
        self.pieces = [Piece.Piece(symbol2, 1, 1, 2, False), Piece.Piece(symbol1, 3, 3, 1, False)]

# def main():
#
#
#
# if __name__ == "__main__":
#     main()
