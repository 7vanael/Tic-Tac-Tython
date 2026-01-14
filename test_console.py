import pytest
from board import Board
from console import render_board, render_welcome, interleave_numbers

@pytest.fixture
def board():
    return Board()

def test_print_output(capsys):
    render_welcome()
    captured = capsys.readouterr()
    assert captured.out == 'Welcome to Tic-Tac-Tython!\n Let\'s play!\n'

class TestInterleaveNumbers:
    def test_print_full_board(self, board):
        board.cells = [
        "X", "O", "X",
        "X", "X", "O",
        "O", "X", "O",
    ]
        assert interleave_numbers(board.cells) == board.cells

    def test_print_empty_board(self, board):
        board.cells = [
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " ",
    ]
        assert interleave_numbers(board.cells) == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def test_print_partially_occupied_board(self, board):
        board.cells = [
        "X", "O", "X",
        " ", "O", " ",
        " ", "X", " ",
    ]
        assert interleave_numbers(board.cells) == ["X", "O", "X", "4", "O", "6", "7", "X", "9"]


def test_print_empty_board(capsys, board):
    render_board(board)
    captured = capsys.readouterr()
    assert captured.out == "1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n\n"

def test_print_full_board(capsys, board):
    board.cells = [
        "X", "O", "X",
        "X", "X", "O",
        "O", "X", "O",
    ]
    render_board(board)
    captured = capsys.readouterr()
    assert captured.out == "X | O | X\n---------\nX | X | O\n---------\nO | X | O\n\n"