import Piece


class Board:

    def __init__(self):
        self.pieces = [Piece.Piece() for x in range(17)]

    def set_up_board(self):
        pass

    def draw_board(self):
        pass

    def space_occupied(self):
        pass

    def can_capture_piece(self):
        pass

# def main():
#     print(Board().pieces[0].symbol)
#
#
# if __name__ == "__main__":
#     main()
