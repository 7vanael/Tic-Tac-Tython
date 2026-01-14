import pytest
from unittest.mock import patch
from tic_tac_toe.player.human_player import HumanPlayer
from tic_tac_toe.board import Board

@pytest.fixture
def board():
    return Board()
@pytest.fixture
def human_x():
    return HumanPlayer(Board.PLAYER_X)

class TestHumanMove:
    def test_human_move_returns_valid_move(self, board, human_x):
        with patch('builtins.input', return_value='1'):
            move = human_x.get_move(board)
            assert move == 0

    def test_human_move_rejects_invalid_number(self, board, human_x):
        with (patch('builtins.input', side_effect=['10', '-1', '1']),
              patch('builtins.print') as mock_print):
            move = human_x.get_move(board)
            assert move == 0
            assert mock_print.call_count == 2

    def test_human_move_rejects_non_numeric_input(self, board, human_x):
        with (patch('builtins.input', side_effect=['abc', 'x', '1']),
              patch('builtins.print') as mock_print):
            move = human_x.get_move(board)
            assert move == 0
            assert mock_print.call_count == 2

    def test_human_move_rejects_already_taken_position(self, board, human_x):
        board.make_move(0, Board.PLAYER_X)
        with (patch('builtins.input', side_effect=['1', '2']),
              patch('builtins.print') as mock_print):
            move = human_x.get_move(board)
            assert move == 1
            mock_print.assert_called_with("Invalid move. Try again.")

