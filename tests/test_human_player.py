import pytest
from unittest.mock import MagicMock
from player_human import HumanPlayer
from board import Board

@pytest.fixture
def notifier():
    return MagicMock()

@pytest.fixture
def board():
    return Board()

@pytest.fixture
def human_x(notifier):
    return HumanPlayer(Board.PLAYER_X, notifier)

class TestHumanMove:
    def test_human_move_returns_valid_move(self, board, human_x, notifier):
        notifier.prompt_for_move.return_value = "1"
        move = human_x.select_move(board)
        assert move == 0
        notifier.prompt_for_move.assert_called_once_with(Board.PLAYER_X)
        notifier.announce_move.assert_called_once_with(Board.PLAYER_X, 0)
        notifier.notify_invalid_move.assert_not_called()

    def test_human_move_rejects_invalid_number(self, board, human_x, notifier):
        notifier.prompt_for_move.side_effect = ["10", "-1", "1"]
        move = human_x.select_move(board)
        assert move == 0
        assert notifier.notify_invalid_move.call_count == 2
        notifier.announce_move.assert_called_once_with(Board.PLAYER_X, 0)

    def test_human_move_rejects_non_numeric_input(self, board, human_x, notifier):
        notifier.prompt_for_move.side_effect = ["abc", "x", "1"]
        move = human_x.select_move(board)
        assert move == 0
        assert notifier.notify_invalid_move.call_count == 2
        notifier.announce_move.assert_called_once_with(Board.PLAYER_X, 0)

    def test_human_move_rejects_already_taken_position(self, board, human_x, notifier):
        board.make_move(0, Board.PLAYER_X)
        notifier.prompt_for_move.side_effect = ["1", "2"]
        move = human_x.select_move(board)
        assert move == 1
        notifier.notify_invalid_move.assert_called_once()
        notifier.announce_move.assert_called_once_with(Board.PLAYER_X, 1)
