from Piece import Piece

class King(Piece):

    def get_valid_moves(self):
        """
        Checks for the positions of immediately-located squares on the diagonals nearby the current piece
        :return: The coordinates of squares a piece may move to in a nested array object
        """
        valid_moves = [[self.row + 1, self.col + 1],
                       [self.row + 1, self.col - 1],
                       [self.row - 1, self.col - 1],
                       [self.row - 1, self.col + 1]]
        return valid_moves



# def main():
#     king = King('O', 1, 1, 1)
#     print(king.symbol)
#
#
#
# if __name__ == "__main__":
#     main()