from abc import ABC, abstractmethod
from board import Board


class Player(ABC):
    def __init__(self, character: str, notifier):
        self.character = character
        self.notifier = notifier

    @abstractmethod
    def select_move(self, board: Board) -> int:
        raise NotImplementedError