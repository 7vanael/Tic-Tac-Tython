from typing import List, Optional

class Board:
    EMPTY = " "
    PLAYER_X = "X"
    PLAYER_O = "O"

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
