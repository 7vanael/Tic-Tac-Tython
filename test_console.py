import pytest
from board import Board
from console import render_board, render_welcome


def test_print_output(capsys):
    render_welcome()
    captured = capsys.readouterr()
    assert captured.out == 'Welcome to Tic-Tac-Tython!\n Let\'s begin:  \n'

def test_print_empty_board(capsys):
    board = Board()
    render_board(board)
    captured = capsys.readouterr()
    assert captured.out == "1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n"