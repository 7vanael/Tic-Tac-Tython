from tests.conftest import game_x_win
from tic_tac_toe.board import Board

def test_game_initialization(game_x_win):
    game, _ = game_x_win
    assert len(game.board.cells) == 9
    assert all(cell == Board.EMPTY for cell in game.board.cells)

def test_game_detects_winner(game_x_win):
    game, _ = game_x_win
    game.board.cells = [
        "X", "X", "X",
        " ", " ", " ",
        " ", " ", " "
    ]
    assert game.board.winner() == "X"


def test_game_draw_state(game_draw):
    game, _ = game_draw
    game.board.cells = [
        "X", "O", "X",
        "X", "O", "O",
        "O", "X", "X"
    ]
    assert game.board.is_end_state()
    assert game.board.winner() is None

class TestPlay:
    def test_play_alternates_between_players(self, game_x_win):
        game, _ = game_x_win
        game.play()
        assert game.board.cells[0] == Board.PLAYER_X
        assert game.board.cells[3] == Board.PLAYER_O
        assert game.board.cells[1] == Board.PLAYER_X
        assert game.board.cells[4] == Board.PLAYER_O
        assert game.board.cells[2] == Board.PLAYER_X

    def test_play_renders_board_each_turn(self, game_x_win):
        game, notifier = game_x_win
        game.play()

        assert notifier.render_board.call_count == 6

    def test_play_displays_winner_when_x_wins(self, game_x_win):
        game, notifier = game_x_win
        game.play()

        notifier.notify_winner.assert_called_once_with(Board.PLAYER_X)
        assert game.board.is_end_state()

    def test_play_displays_draw_when_board_full(self, game_draw):
        game, notifier = game_draw
        game.play()

        assert game.board.winner() is None
        notifier.notify_winner.assert_called_once_with(None)
        assert game.board.is_end_state()