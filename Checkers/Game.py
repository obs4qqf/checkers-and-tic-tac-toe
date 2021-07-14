import Board


class Game:

    def __init__(self):
        self.Board = Board.Board()
        self.player1_turn = True


    def draw_board(self):
        for row in self.board:
            print(f'{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}|{row[6]}|{row[7]}')


    def pick_piece(self):
        need_piece = True
        while need_piece:
            pass

    def player_move(self):
        pass

def main():
    game = Game()
    game.draw_board()
    while not game.game_won:
        if game.player_turn:
            pass
        else:
            pass

if __name__ == "__main__":
    main()