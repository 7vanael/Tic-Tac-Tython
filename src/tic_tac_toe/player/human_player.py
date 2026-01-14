from tic_tac_toe.board import Board
from tic_tac_toe.player.player import Player


class HumanPlayer(Player):
    def get_move(self, board: Board) -> int:
        while True:
            try:
                move = int(input("Choose a move (1-9): ")) - 1
                if move in board.available_moves():
                    return move
            except ValueError:
                pass
            print("Invalid move. Try again.")