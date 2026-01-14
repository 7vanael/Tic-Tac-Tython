from abc import ABC, abstractmethod
from tic_tac_toe.board import Board


class Player(ABC):
    def __init__(self, character: str):
        self.character = character

    @abstractmethod
    def get_move(self, board: Board) -> int:
        raise NotImplementedError