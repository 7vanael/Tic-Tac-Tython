import random

from board import Board
from player import Player


class EasyAi(Player):
    def select_move(self, board: Board) -> int:
        move = random.choice(board.available_moves())
        self.notifier.announce_move(self.character, move)
        return move