import pytest
from unittest.mock import patch
from tic_tac_toe.board import Board
from tic_tac_toe.console import CliNotifier

@pytest.fixture
def board():
    return Board()
@pytest.fixture
def notify():
    return CliNotifier()

def test_print_output(capsys, notify):
    notify.render_welcome()
    captured = capsys.readouterr()
    assert captured.out == 'Welcome to Tic-Tac-Tython!\n Let\'s play!\n'

class TestSelectPlayerType:
    def test_select_player_type_returns_correct_choice(self, capsys, notify):
        with patch("builtins.input", side_effect=["foo", "-4", "* 0", " human  ", "1"]):
            choice = notify.select_player_type(Board.PLAYER_X, {"human": "Human", "ai_hard": "Hard AI"})

        assert choice == "human"

        captured = capsys.readouterr()
        invalid_message = "Invalid choice. Please enter a number between 1 and 2."
        assert "Enter a number to select player type for X:" in captured.out
        assert "1. Human" in captured.out
        assert "2. Hard AI" in captured.out
        assert "Enter selection: " in captured.out
        assert 4 == captured.out.count(invalid_message)

class TestInterleaveNumbers:
    def test_print_full_board(self, board, notify):
        board.cells = [
        "X", "O", "X",
        "X", "X", "O",
        "O", "X", "O",
    ]
        assert notify._interleave_numbers(board.cells) == board.cells

    def test_print_empty_board(self, board, notify):
        board.cells = [
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " ",
    ]
        assert notify._interleave_numbers(board.cells) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def test_print_partially_occupied_board(self, board, notify):
        board.cells = [
        "X", "O", "X",
        " ", "O", " ",
        " ", "X", " ",
    ]
        assert notify._interleave_numbers(board.cells) == ["X", "O", "X", "4", "O", "6", "7", "X", "9"]


def test_print_empty_board(capsys, board, notify):
    notify.render_board(board)
    captured = capsys.readouterr()
    assert captured.out == "1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n\n"

def test_print_full_board(capsys, board, notify):
    board.cells = [
        "X", "O", "X",
        "X", "X", "O",
        "O", "X", "O",
    ]
    notify.render_board(board)
    captured = capsys.readouterr()
    assert captured.out == "X | O | X\n---------\nX | X | O\n---------\nO | X | O\n\n"