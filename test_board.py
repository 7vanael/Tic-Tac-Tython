import pytest
from board import Board


class TestBoardInitialization:
    def test_new_board_has_9_empty_cells(self):
        board = Board()
        assert len(board.cells) == 9
        assert all(cell == Board.EMPTY for cell in board.cells)


class TestAvailableMoves:
    def test_new_board_has_all_positions_available(self):
        board = Board()
        assert board.available_moves() == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def test_board_with_one_move_has_eight_available(self):
        board = Board()
        board.cells[0] = Board.PLAYER_X
        assert board.available_moves() == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_board_with_scattered_moves(self):
        board = Board()
        board.cells[1] = Board.PLAYER_X
        board.cells[4] = Board.PLAYER_O
        board.cells[7] = Board.PLAYER_X
        assert board.available_moves() == [0, 2, 3, 5, 6, 8]

    def test_full_board_has_no_available_moves(self):
        board = Board()
        board.cells = [Board.PLAYER_X if i % 2 == 0 else Board.PLAYER_O for i in range(9)]
        assert board.available_moves() == []


class TestMakeMove:
    def test_make_move_on_empty_cell(self):
        board = Board()
        board.make_move(0, Board.PLAYER_X)
        assert board.cells[0] == Board.PLAYER_X

    def test_make_move_updates_correct_position(self):
        board = Board()
        board.make_move(4, Board.PLAYER_O)
        assert board.cells[4] == Board.PLAYER_O
        assert board.cells[3] == Board.EMPTY
        assert board.cells[5] == Board.EMPTY

    def test_make_move_on_occupied_cell_raises_error(self):
        board = Board()
        board.cells[0] = Board.PLAYER_X
        with pytest.raises(ValueError, match="Invalid move"):
            board.make_move(0, Board.PLAYER_O)

    def test_make_move_with_invalid_index_raises_error(self):
        board = Board()
        with pytest.raises(ValueError, match="Invalid move"):
            board.make_move(9, Board.PLAYER_X)

    def test_make_move_with_negative_index_raises_error(self):
        board = Board()
        with pytest.raises(ValueError, match="Invalid move"):
            board.make_move(-1, Board.PLAYER_X)


class TestIsFull:
    def test_new_board_is_not_full(self):
        board = Board()
        assert not board.is_full()

    def test_board_with_one_move_is_not_full(self):
        board = Board()
        board.cells[0] = Board.PLAYER_X
        assert not board.is_full()

    def test_board_with_eight_moves_is_not_full(self):
        board = Board()
        for i in range(8):
            board.cells[i] = Board.PLAYER_X if i % 2 == 0 else Board.PLAYER_O
        assert not board.is_full()

    def test_completely_filled_board_is_full(self):
        board = Board()
        board.cells = [Board.PLAYER_X if i % 2 == 0 else Board.PLAYER_O for i in range(9)]
        assert board.is_full()

