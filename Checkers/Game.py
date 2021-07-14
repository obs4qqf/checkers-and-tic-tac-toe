import Board


class Game:

    def __init__(self, symbol1, symbol2):
        self.board = Board.Board(symbol1, symbol2)
        self.player1_turn = True


    def game_won(self):
        pass

    def pick_piece(self):
        need_piece = True
        while need_piece:
            pass

def main():
    game = Game('O', 'X')
    game.board.draw_board()
    # while not game.game_won:
    #     if game.player1_turn:
    #         pass
    #     else:
    #         pass

if __name__ == "__main__":
    main()