from unittest.mock import MagicMock
import pytest
from tic_tac_toe.board import Board
from tic_tac_toe.player.ai_player import HardAI


@pytest.fixture
def notifier():
    return MagicMock()

@pytest.fixture
def board():
    return Board()
@pytest.fixture
def ai_o(notifier):
    return HardAI(Board.PLAYER_O, notifier)

class TestScore:
    def test_scores_immediate_win_10(self, board, ai_o):
        board.cells = [
            "X", "O", " ",
            "X", "O", " ",
            " ", "O", "X"
        ]
        score = HardAI.calculate_terminal_score(ai_o, board, depth=0)
        assert score == 10

    def test_scores_faster_win_higher_than_slower(self, board, ai_o):
        board.cells = [
            "X", "O", " ",
            "X", "O", " ",
            " ", "O", "X"
        ]
        score_depth_0 = HardAI.calculate_terminal_score(ai_o, board, depth=0)
        score_depth_3 = HardAI.calculate_terminal_score(ai_o, board, depth=3)
        score_depth_5 = HardAI.calculate_terminal_score(ai_o, board, depth=5)
        assert score_depth_0 > score_depth_3 > score_depth_5
        assert score_depth_0 == 10
        assert score_depth_3 == 7
        assert score_depth_5 == 5

    def test_scores_immediate_loss_negative_10(self, board, ai_o):
        board.cells = [
            "O", "X", " ",
            "O", "X", " ",
            " ", "X", " "
        ]
        score = HardAI.calculate_terminal_score(ai_o, board, depth=0)
        assert score == -10

    def test_scores_delayed_loss_less_negative(self, board, ai_o):
        board.cells = [
            "O", "X", " ",
            "O", "X", " ",
            " ", "X", " "
        ]
        score_depth_0 = HardAI.calculate_terminal_score(ai_o, board, depth=0)
        score_depth_3 = HardAI.calculate_terminal_score(ai_o, board, depth=3)
        score_depth_5 = HardAI.calculate_terminal_score(ai_o, board, depth=5)
        assert score_depth_0 < score_depth_3 < score_depth_5
        assert score_depth_0 == -10
        assert score_depth_3 == -7
        assert score_depth_5 == -5

    def test_score_tie_is_zero(self, board, ai_o):
        board.cells = [
            "X", "O", "X",
            "X", "O", "O",
            "O", "X", "X"
        ]
        score_depth_0 = HardAI.calculate_terminal_score(ai_o, board, depth=0)
        score_depth_3 = HardAI.calculate_terminal_score(ai_o, board, depth=3)
        score_depth_5 = HardAI.calculate_terminal_score(ai_o, board, depth=5)
        assert score_depth_0 == score_depth_3 == score_depth_5 == 0


class TestHardAI:
    def test_ai_blocks_immediate_loss(self, board, ai_o):
        board.cells = [
            "X", "X", " ",
            " ", "O", " ",
            " ", " ", " "
        ]
        move = ai_o.select_move(board)
        assert move == 2


    def test_ai_takes_fastest_winning_move(self, board, ai_o):
        board.cells = [
            "O", "O", " ",
            "X", "X", " ",
            " ", " ", " "
        ]
        move = ai_o.select_move(board)
        assert move == 2


    def test_ai_still_selects_valid_move_when_equivalent(self, board, ai_o):
        board.cells = [
            "X", "O", "X",
            "X", "O", " ",
            "O", "X", " "
        ]
        move = ai_o.select_move(board)
        assert move in board.available_moves()

    def test_ai_takes_corner_to_open(self, board, ai_o):
        move = ai_o.select_move(board)
        assert move in {0, 2, 6, 8}

    def test_ai_takes_center_if_x_opens_corner(self, board, ai_o):
        board.cells[0] = "X"
        move = ai_o.select_move(board)
        assert move == 4


    def test_ai_prevents_fork(self, board, ai_o):
        board.cells = [
            "X", " ", " ",
            " ", "O", " ",
            " ", " ", "X"
        ]
        move = ai_o.select_move(board)
        assert move in {1, 3, 5, 7}

    def test_ai_does_not_mutate_board(self, board, ai_o):
        original = board.cells.copy()
        ai_o.select_move(board)
        assert board.cells == original

    def test_ai_notifies_move(self, board, ai_o):
        board.cells[0] = "X"
        move = ai_o.select_move(board)
        assert move == 4
        ai_o.notifier.announce_move.assert_called_once_with(Board.PLAYER_O, 4)