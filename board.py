from typing import List, Optional

class Board:
    EMPTY = " "
    PLAYER_X = "X"
    PLAYER_O = "O"

    WIN_COMBINATIONS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    def __init__(self):
        self.cells = [self.EMPTY] * 9

    def available_moves(self) -> List[int]:
        return [i for i, cell in enumerate(self.cells) if cell == self.EMPTY]

    def make_move(self, index: int, player: str):
        if index not in self.available_moves():
            raise ValueError("Invalid move")
        self.cells[index] = player

    def is_full(self) -> bool:
        return self.EMPTY not in self.cells
