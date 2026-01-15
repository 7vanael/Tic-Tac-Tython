import pytest
from board import Board


@pytest.fixture
def board():
    return Board()

def test_new_board_has_9_empty_cells():
    board = Board()
    assert len(board.cells) == 9
    assert all(cell == Board.EMPTY for cell in board.cells)


class TestAvailableMoves:
    def test_new_board_has_all_positions_available(self, board):
        assert board.available_moves() == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def test_board_with_one_move_has_eight_available(self, board):
        board.cells[0] = Board.PLAYER_X
        assert board.available_moves() == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_board_with_scattered_moves(self, board):
        board.cells[1] = Board.PLAYER_X
        board.cells[4] = Board.PLAYER_O
        board.cells[7] = Board.PLAYER_X
        assert board.available_moves() == [0, 2, 3, 5, 6, 8]

    def test_full_board_has_no_available_moves(self, board):
        board.cells = [Board.PLAYER_X if i % 2 == 0 else Board.PLAYER_O for i in range(9)]
        assert board.available_moves() == []


class TestMakeMove:
    def test_make_move_on_empty_cell(self, board):
        board.make_move(0, Board.PLAYER_X)
        assert board.cells[0] == Board.PLAYER_X

    def test_make_move_updates_correct_position(self, board):
        board.make_move(4, Board.PLAYER_O)
        assert board.cells[4] == Board.PLAYER_O
        assert board.cells[3] == Board.EMPTY
        assert board.cells[5] == Board.EMPTY

    def test_make_move_on_occupied_cell_raises_error(self, board):
        board.cells[0] = Board.PLAYER_X
        with pytest.raises(ValueError, match="Invalid move"):
            board.make_move(0, Board.PLAYER_O)

    def test_make_move_with_invalid_index_raises_error(self, board):
        with pytest.raises(ValueError, match="Invalid move"):
            board.make_move(9, Board.PLAYER_X)

    def test_make_move_with_negative_index_raises_error(self, board):
        with pytest.raises(ValueError, match="Invalid move"):
            board.make_move(-1, Board.PLAYER_X)


class TestIsFull:
    def test_new_board_is_not_full(self, board):
        assert not board.is_full()
        assert not board.is_end_state()

    def test_board_with_one_move_is_not_full(self, board):
        board.cells[0] = Board.PLAYER_X
        assert not board.is_full()
        assert not board.is_end_state()

    def test_board_with_eight_moves_is_not_full(self, board):
        for i in range(8):
            board.cells[i] = Board.PLAYER_X if i % 2 == 0 else Board.PLAYER_O
        assert not board.is_full()

    def test_completely_filled_board_is_full(self, board):
        board.cells = [Board.PLAYER_X if i % 2 == 0 else Board.PLAYER_O for i in range(9)]
        assert board.is_full()
        assert board.is_end_state()

class TestWinner:
    def test_empty_board_no_winner(self, board):
        assert board.winner() is None
        assert not board.is_end_state()

    def test_two_cells_no_winner(self, board):
        board.cells[0] = Board.PLAYER_X
        board.cells[1] = Board.PLAYER_O
        assert board.winner() is None
        assert not board.is_end_state()

    def test_two_matching_cells_no_winner(self, board):
        board.cells[0] = Board.PLAYER_X
        board.cells[1] = Board.PLAYER_X
        assert board.winner() is None

    def test_row_012_wins_x(self, board):
        board.cells[0] = Board.PLAYER_X
        board.cells[1] = Board.PLAYER_X
        board.cells[2] = Board.PLAYER_X
        assert board.winner() == "X"
        assert board.is_end_state()

    def test_row_012_wins_o(self, board):
        board.cells[0] = Board.PLAYER_O
        board.cells[1] = Board.PLAYER_O
        board.cells[2] = Board.PLAYER_O
        assert board.winner() == "O"
        assert board.is_end_state()

    def test_win_combinations(self, board):
        assert Board.WIN_COMBINATIONS == [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                          (0, 4, 8), (2, 4, 6)]

    @pytest.mark.parametrize("combo", Board.WIN_COMBINATIONS)
    @pytest.mark.parametrize("player", [Board.PLAYER_X, Board.PLAYER_O])
    def test_all_winning_combinations(self, board, combo, player):
        a, b, c = combo
        board.cells[a] = player
        board.cells[b] = player
        board.cells[c] = player
        assert board.winner() == player
        assert board.is_end_state()

    def test_no_winning_combinations(self, board):
        board.cells = [
            "X", "O", "X",
            "O", "X", "X",
            "O", "X", "O"
        ]
        assert board.winner() is None
        assert board.is_end_state()


class TestTie:
    def test_full_board_no_winner(self, board):
        board.cells = [
            "X", "O", "X",
            "O", "X", "X",
            "O", "X", "O"
        ]
        assert board.winner() is None
        assert board.is_full()
        assert board.is_end_state()


class TestClearCell:
    def test_empty_cell(self, board):
        board.clear_cell(0)
        assert board.cells[0] == Board.EMPTY

    def test_occupied_cell(self, board):
        board.cells[0] = Board.PLAYER_X
        board.clear_cell(0)
        assert board.cells[0] == Board.EMPTY
