from tic_tac_toe.board import Board
from tic_tac_toe.player.player import Player


class HumanPlayer(Player):
    def select_move(self, board: Board) -> int:
        while True:
            try:
                choice = self.notifier.prompt_for_move(self.character)
                move = int(choice) - 1
                if move in board.available_moves():
                    self.notifier.announce_move(self.character, move)
                    return move
            except ValueError:
                pass
            self.notifier.notify_invalid_move(self.character, board)