import pygame

class CheckersGame:

    def __init__(self):
        self.piece1 = 'O'
        self.piece2 = 'X'
        self.board = [[self.piece2 for x in range(9)],
                      [self.piece2 for x in range(9)],
                      [' ' for x in range(9)],
                      [' ' for x in range(9)],
                      [' ' for x in range(9)],
                      [' ' for x in range(9)],
                      [self.piece1 for x in range(9)],
                      [self.piece1 for x in range(9)]]
        self.player_turn = True
        self.game_won = False


    def draw_board(self):
        pygame.draw.rect()
        # for row in self.board:
        #     print(f'{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}|{row[6]}|{row[7]}')


    def pick_piece(self):
        need_piece = True
        while need_piece:
            pass

    def player_move(self):
        pass

def main():
    # game = CheckersGame()
    # game.draw_board()
    # while not game.game_won:
    #     if game.player_turn:
    #         pass
    #     else:
    #         pass

    pygame.display.set_mode((400, 400))
    game = CheckersGame()
    clock = pygame.time.Clock()
    while not game.game_won:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_won = True
    pygame.quit()

if __name__ == "__main__":
    main()