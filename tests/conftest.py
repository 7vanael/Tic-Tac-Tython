import pytest
from unittest.mock import Mock, MagicMock
from tic_tac_toe.board import Board
from tic_tac_toe.game import Game
from tic_tac_toe.player.player import Player

@pytest.fixture
def notifier():
    return MagicMock()

class EmptyFakePlayer(Player):
    def __init__(self, character: str, notifier):
        super().__init__(character, notifier)
    def select_move(self, board: Board):
        return 0

class FakePlayer(Player):
    def __init__(self, character: str, notifier, moves):
        super().__init__(character, notifier)
        self.moves = iter(moves)

    def select_move(self, board):
        return next(self.moves)

@pytest.fixture
def game_x_win(notifier):
    board = Board()
    players = {
        Board.PLAYER_X: FakePlayer(Board.PLAYER_X, notifier,[0, 1, 2]),
        Board.PLAYER_O: FakePlayer(Board.PLAYER_O, notifier, [3, 4, 5])
    }
    game = Game(board, players, notifier)
    return game, notifier

@pytest.fixture
def game_draw(notifier):
    board = Board()
    players = {
        Board.PLAYER_X: FakePlayer(Board.PLAYER_X, notifier, [0, 2, 7, 3, 5]),
        Board.PLAYER_O: FakePlayer(Board.PLAYER_O, notifier, [4, 1, 8, 6])
    }
    game = Game(board, players, notifier)
    return game, notifier