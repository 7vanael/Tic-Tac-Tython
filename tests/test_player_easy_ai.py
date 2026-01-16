from unittest.mock import MagicMock, patch
import pytest
from board import Board
from player_easy_ai import EasyAi


@pytest.fixture
def notifier():
    return MagicMock()

@pytest.fixture
def board():
    return Board()


@pytest.fixture
def random_x(notifier):
    return EasyAi(Board.PLAYER_X, notifier)


def test_random_player_returns_available_move(board, random_x):
    move = random_x.select_move(board)
    assert move in board.available_moves()

def test_random_player_announces_move(board, random_x, notifier):
    with patch("player_easy_ai.random.choice", return_value=3):
        move = random_x.select_move(board)

    assert move == 3
    notifier.announce_move.assert_called_once_with(Board.PLAYER_X, 3)

def test_random_player_respects_taken_positions(board, random_x):
    board.make_move(0, Board.PLAYER_X)
    board.make_move(4, Board.PLAYER_O)

    move = random_x.select_move(board)

    assert move in board.available_moves()
    assert move not in [0, 4]

def test_random_player_uses_available_moves(board, random_x):
    with patch("player_easy_ai .random.choice") as mock_choice:
        mock_choice.return_value = 2
        random_x.select_move(board)

    mock_choice.assert_called_once_with(board.available_moves())