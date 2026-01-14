import pytest
from unittest.mock import Mock
from tic_tac_toe.board import Board
from tic_tac_toe.game import Game
from tic_tac_toe.player.player import Player

class FakePlayer(Player):
    def __init__(self, character: str, moves):
        super().__init__(character)
        self.moves = iter(moves)

    def get_move(self, board):
        return next(self.moves)

@pytest.fixture
def game_x_win():
    board = Board()
    players = {
        Board.PLAYER_X: FakePlayer(Board.PLAYER_X, [0, 1, 2]),
        Board.PLAYER_O: FakePlayer(Board.PLAYER_O, [3, 4, 5])
    }
    notifier = Mock()
    game = Game(board, players, notifier)
    return game, notifier

@pytest.fixture
def game_draw():
    board = Board()
    players = {
        Board.PLAYER_X: FakePlayer(Board.PLAYER_X, [0, 2, 7, 3, 5]),
        Board.PLAYER_O: FakePlayer(Board.PLAYER_O, [4, 1, 8, 6])
    }
    notifier = Mock()
    game = Game(board, players, notifier)
    return game, notifier