import Board
import math

class Game:
    """
    Defines basic board game objects and general checkers game methods.
    """

    def __init__(self, symbol1, symbol2):
        """
        Creates a Game object to begin checkers game
        :param symbol1: Player 1's marker symbol as a string
        :param symbol2: Player 2's marker symbol as a string
        """
        self.board = Board.Board(symbol1, symbol2)
        self.player1_turn = True


    def game_won(self):
        """
        Checks if the game is won (if no moves are left or if a player loses all pieces)
        :return: Whether the game has been won as a boolean
        """
        if self.board.player_has_no_pieces():
            return True
        moves_available_1 = False  # Tracks whether player 1 still has moves left to make
        moves_available_2 = False
        for piece in self.board.pieces:
            if self.board.can_move_piece(piece) and piece.alive and piece.player == 1:
                moves_available_1 = True  # The player can move an active piece
        for piece in self.board.pieces:
            if self.board.can_move_piece(piece) and piece.alive and piece.player == 2:
                moves_available_2 = True
        # If moves are available (True), the game is not won, so game_won should return False
        return not (moves_available_1 and moves_available_2)

    def pick_piece(self, player):
        """
        Allows the player to pick a piece and checks if that piece is valid to pick
        :param player: The current player as an integer
        :return: The chosen piece as a Piece object
        """
        need_piece = True
        while need_piece:
            row = input('Pick pick a row with your piece (1-8): ')
            col = input('Pick pick a column with your piece (1-8): ')
            try:
                row = int(row)
                col = int(col)
                if 0 < row < 9 and 0 < col < 9:
                    row -= 1  # Converts row/column number from 1-8 scale to be on 0-7 scale
                    col -= 1
                    if self.board.space_occupied(row, col):
                        piece = self.board.get_piece_at_space(row, col)
                        if piece.player == player:
                            if self.board.can_move_piece(piece):  # Checks if piece can move/capture another piece
                                print('Piece selected!')
                                return self.board.get_piece_at_space(row, col)
                            else:
                                print('ERROR: Pick a piece that can be moved')
                        else:
                            print('ERROR: Pick a space with your piece')
                    else:
                        print('ERROR: Pick a space with a marker')
                else:
                    print('ERROR: Pick a number in the appropriate ranges')
            except:
                print('ERROR: Pick a number')

    def move_piece(self, piece):
        """
        Moves the selected piece to a valid nearby location that the player defines
        :param piece: The piece selected previously as a Piece object
        """
        need_move = True
        while need_move:
            row = input('Pick pick a row to move your piece to or to capture a piece (1-8): ')
            col = input('Pick pick a column to move your piece to or to capture a piece (1-8): ')
            try:
                row = int(row)
                col = int(col)
                row -= 1  # Converts row/column number from 1-8 scale to be on 0-7 scale
                col -= 1
                if [row, col] in piece.get_valid_moves():  # Checks if space chosen is diagonally located to piece
                    if not self.board.space_occupied(row, col):
                        piece.row = row
                        piece.col = col
                        need_move = False
                    else:
                        nearby_piece = self.board.get_piece_at_space(row, col)
                        if nearby_piece.player != piece.player:  # Checks if space is occupied by opponent's piece
                            if self.board.can_capture_piece(piece, nearby_piece):
                                piece.capture_piece(nearby_piece)
                                need_move = False
                            else:
                                print('ERROR: The piece you have selected cannot be captured')
                        else:  # This is entered if space is occupied by player's own marker
                            print('ERROR: Pick a space without your marker')
                else:
                    print('ERROR: Pick a valid space nearby your piece')
            except:
                print('ERROR: Pick a number')

    def restart_game_prompt(self):
        """
        Asks the player whether they would like to continue the game after a win/loss
        :return:
        """
        need_answer = True
        while need_answer:
            answer = input('Do you want to play again? (Yes/No) ')
            if answer == 'Yes':
                need_answer = False
                return True
            elif answer == 'No':
                need_answer = False
                return False
            else:
                print('ERROR: Input not defined, please enter Yes or No')

    def comp_move(self):
        """
        Allows the computer to pick and move a checkers piece using minimax algorithm
        :return: The best piece for the computer to move
        """
        best_turn = self.minimax(0, 2)
        if best_turn['move'][2]:  # This is entered if the best move is a piece-capturing move
            best_turn['piece'].capture_piece(best_turn['move'][2])
        else:  # This is entered if the best move is a change in location
            best_turn['piece'].row = best_turn['move'][0]
            best_turn['piece'].col = best_turn['move'][1]
        return best_turn['piece']

    def minimax(self, depth, player):
        """
        Determines the best possible move that can be made for the near future using recursion
        :param depth: The amount of future events that should be considered as an integer
        :param player: The player's possible future decisions that are being analyzed
        :return: A dictionary including the best score, best piece to move, and best position to move the piece to
        """
        if player == 1:  # This is entered for the human player (minimizing player)
            best_score = math.inf
        else:  # This is enter for the computer player (maximizing player)
            best_score = -math.inf
        best_move = {'piece': None, 'move': [0, 0, None]}
        if depth >= 3:  # Base case that considers the difference in pieces between the two players
            best_turn = {
                'best_score': self.board.get_pieces_amount(2) - self.board.get_pieces_amount(1),
                'piece': best_move['piece'],
                'move': best_move['move']
            }
            # print(self.board.get_pieces_amount(2) - self.board.get_pieces_amount(1), 'depth', depth, 'player',player)
            print(best_turn,'base')
            return best_turn
        for piece in self.board.pieces:
            if self.board.can_move_piece(piece) and piece.player == player:
                for move in self.board.get_available_moves(piece):
                    print(move, player)
                    # print('move:',move,',player:',player,',depth:',depth)
                    old_row = piece.row  # This stores the current position of a piece so it can be moved back later
                    old_col = piece.col
                    if move[2]:  # This is entered if the current analyzed move is a capturing move
                        piece.capture_piece(move[2])
                    else:  # This is entered if the current move is just a change in location
                        piece.row = move[0]
                        piece.col = move[1]
                    self.board.make_piece_king(piece)
                    if player == 1:
                        next_player = 2
                    else:
                        next_player = 1
                    score = self.minimax(depth + 1, next_player)['best_score']
                    print('score',score)
                    if move[2]:
                        move[2].alive = True  # This makes the captured piece alive again to reset the board
                    piece.row = old_row  # This moves the moved piece back to its original position
                    piece.col = old_col
                    if piece.king:
                        piece.king = False
                    if player == 1:
                        if score < best_score:  # Finds the min score
                            best_score = score
                            best_move['piece'] = piece
                            best_move['move'] = move
                    else:
                        if score > best_score:  # Finds the max score
                            best_score = score
                            best_move['piece'] = piece
                            best_move['move'] = move
        best_turn = {
            'best_score': best_score,
            'piece': best_move['piece'],
            'move': best_move['move']
        }
        print(best_turn,'outside')
        print('depth',depth,'player',player)
        return best_turn



def main():
    """
    Defines the main game loop
    """
    symbol1 = 'O'
    symbol2 = 'X'
    game_on = True
    while game_on:
        game = Game(symbol1, symbol2)
        game.board.init_piece_positions(symbol1, symbol2)  # used for debugging purposes to pick chess piece positions
        game.player1_turn = True  # used for debugging purposes
        game.board.draw_board()
        print('Welcome to Checkers')
        while not game.game_won():
            if game.player1_turn:
                print('Player 1 turn, piece symbol:', symbol1)
                piece = game.pick_piece(1)
                game.move_piece(piece)
                game.board.make_piece_king(piece)
                game.board.draw_board()
                if game.game_won():
                    break
                game.player1_turn = False
            else:
                # pass
                print('Player 2 turn, piece symbol:', symbol2)
                piece = game.comp_move()
                game.board.make_piece_king(piece)
                game.board.draw_board()
                if game.game_won():
                    break
                game.player1_turn = True
        if game.player1_turn:
            print('Player 1 has won')
            if not game.restart_game_prompt():
                game_on = False
        else:
            print('Player 2 has won')
            if not game.restart_game_prompt():
                game_on = False
    print('The game has ended')

if __name__ == "__main__":
    main()