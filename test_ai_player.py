import pytest
from board import Board
from ai_player import HardAI


@pytest.fixture
def board():
    return Board()
@pytest.fixture
def ai():
    return HardAI(Board.PLAYER_O)

class TestHardAI:
    def test_ai_blocks_immediate_win(self, board, ai):
        board.cells = [
            "X", "X", " ",
            " ", "O", " ",
            " ", " ", " "
        ]
        move = ai.best_move(board)
        assert move == 2


    def test_ai_takes_fastest_winning_move(self, board, ai):
        board.cells = [
            "O", "O", " ",
            "X", "X", " ",
            " ", " ", " "
        ]
        move = ai.best_move(board)
        assert move == 2


    def test_ai_still_selects_valid_move_when_equivalent(self, board, ai):
        board.cells = [
            "X", "O", "X",
            "X", "O", " ",
            "O", "X", " "
        ]
        move = ai.best_move(board)
        assert move in board.available_moves()

    def test_ai_takes_corner_to_open(self, board, ai):
        move = ai.best_move(board)
        assert move in {0, 2, 6, 8}

    def test_ai_does_not_mutate_board(self, board, ai):
        original = board.cells.copy()
        ai.best_move(board)
        assert board.cells == original