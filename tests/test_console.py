import pytest
from unittest.mock import patch
from board import Board
from console import CliNotifier
from tests.conftest import FakePlayer

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
        with patch("builtins.input", side_effect=["foo", "-4", "* 0", " human  ", "0", "3", "", " ", "1"]):
            choice = notify.select_player_type(Board.PLAYER_X, {"Human": FakePlayer, "Hard AI": FakePlayer})

        assert choice == "Human"

        captured = capsys.readouterr()
        invalid_message = "Invalid choice. Please enter a number between 1 and 2."
        input_prompt = "Enter a number to select player type for X:"
        assert 9 == captured.out.count(input_prompt)
        assert "1. Human" in captured.out
        assert "2. Hard AI" in captured.out
        assert "Enter selection: " in captured.out
        assert 8 == captured.out.count(invalid_message)

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

class TestNotifyWinner:
    def test_print_no_winner(self,capsys, notify):
        notify.notify_winner(None)
        captured = capsys.readouterr()
        assert captured.out == "Draw!\n"

    def test_print_x_winner(self,capsys, notify):
        notify.notify_winner(Board.PLAYER_X)
        captured = capsys.readouterr()
        assert captured.out == "Winner: X!\nGood game!\n"

    def test_print_o_winner(self,capsys, notify):
        notify.notify_winner(Board.PLAYER_O)
        captured = capsys.readouterr()
        assert captured.out == "Winner: O!\nGood game!\n"


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

def test_prompt_for_move_returns_input(notify, board):
    with patch("builtins.input", return_value="5") as mock_input:
        result = notify.prompt_for_move(Board.PLAYER_X)
        mock_input.assert_called_once_with("X, choose a move (1-9): ")
        assert result == "5"

def test_prompt_for_move_returns_any_input(notify, board):
    with patch("builtins.input", return_value="") as mock_input:
        result = notify.prompt_for_move(Board.PLAYER_X)
        mock_input.assert_called_once_with("X, choose a move (1-9): ")
        assert result == ""

def test_notify_invalid_move_prints_message(capsys, notify):
    notify.notify_invalid_move()
    captured = capsys.readouterr()
    assert captured.out == "Invalid move. Please enter a valid move.\n"

def test_announce_move_announces_player_move_plus_1(capsys, notify):
    notify.announce_move(Board.PLAYER_X, 3)
    captured = capsys.readouterr()
    assert captured.out == "X chose move 4\n\n"

def test_play_again_true(capsys, notify):
    with patch("builtins.input", side_effect=["5", "hey", "y"]) as mock_input:
        answer = notify.play_again()
        assert True == answer
        captured = capsys.readouterr()
        invalid_message = "Invalid input"
        assert invalid_message in captured.out
        assert 2 == captured.out.count(invalid_message)
        mock_input.assert_called_with("Would you like to play again? (y/n)\n")
        assert mock_input.call_count == 3


def test_play_again_false(capsys, notify):
    with patch("builtins.input", side_effect=["-3", " ", "n"]) as mock_input:
        answer = notify.play_again()
        assert False == answer
        mock_input.assert_called_with("Would you like to play again? (y/n)\n")
        assert mock_input.call_count == 3
        invalid_message = "Invalid input"
        captured = capsys.readouterr()
        assert invalid_message in captured.out
        assert 2 == captured.out.count(invalid_message)

def test_play_again_retry_limit(capsys, notify):
    with patch("builtins.input", side_effect=["-3", "*", "7", "", "foo"]) as mock_input:
        answer = notify.play_again()
        assert False == answer
        assert mock_input.call_count == 4
        captured = capsys.readouterr()
        invalid_message = "Invalid input"
        assert captured.out.count(invalid_message) == 4
        assert "Too many invalid attempts, I'll assume that's a no! See ya!" in captured.out

@pytest.mark.parametrize("yesses", ["yes", "y", "yeah", "Y", "Yes", "YES"])
def test_play_again_true_options(capsys, notify, yesses):
    with patch("builtins.input", return_value=yesses):
        assert True == notify.play_again()

@pytest.mark.parametrize("nos", ["no", "n", "nah", "N", "No", "NO"])
def test_play_again_true_options(capsys, notify, nos):
    with patch("builtins.input", return_value=nos):
        assert False == notify.play_again()