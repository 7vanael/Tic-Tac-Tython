import pytest
from game import Game
from board import Board
from unittest.mock import patch, call, Mock


def test_game_initialization():
    game = Game()
    assert len(game.board.cells) == 9
    assert all(cell == Board.EMPTY for cell in game.board.cells)


class TestHumanMove:
    def test_human_move_returns_valid_move(self):
        game = Game()
        with patch('builtins.input', return_value='0'):
            move = game._human_move()
            assert move == 0

    def test_human_move_rejects_invalid_number(self):
        game = Game()
        with (patch('builtins.input', side_effect=['9', '-1', '0']),
              patch('builtins.print') as mock_print):
            move = game._human_move()
            assert move == 0
            assert mock_print.call_count == 2  #error messages

    def test_human_move_rejects_non_numeric_input(self):
        game = Game()
        with (patch('builtins.input', side_effect=['abc', 'x', '0']),
              patch('builtins.print') as mock_print):
            move = game._human_move()
            assert move == 0
            assert mock_print.call_count == 2

    def test_human_move_rejects_already_taken_position(self):
        game = Game()
        game.board.make_move(0, Board.PLAYER_X)
        with (patch('builtins.input', side_effect=['0', '1']),
                patch('builtins.print') as mock_print):
            move = game._human_move()
            assert move == 1
            mock_print.assert_called_with("Invalid move. Try again.")


def test_game_alternates_players():
    game = Game()

    game.board.make_move(0, Board.PLAYER_X)
    game.board.make_move(1, Board.PLAYER_O)

    assert game.board.cells[0] == "X"
    assert game.board.cells[1] == "O"


def test_game_detects_winner():
    game = Game()
    game.board.cells = [
        "X", "X", "X",
        " ", " ", " ",
        " ", " ", " "
    ]

    assert game.board.winner() == "X"


def test_game_draw_state():
    game = Game()
    game.board.cells = [
        "X", "O", "X",
        "X", "O", "O",
        "O", "X", "X"
    ]

    assert game.board.is_end_state()
    assert game.board.winner() is None
