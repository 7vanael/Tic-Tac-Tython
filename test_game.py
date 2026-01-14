from game import Game
from board import Board
from unittest.mock import patch


def test_game_initialization():
    game = Game()
    assert len(game.board.cells) == 9
    assert all(cell == Board.EMPTY for cell in game.board.cells)

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

class TestHumanMove:
    def test_human_move_returns_valid_move(self):
        game = Game()
        with patch('builtins.input', return_value='1'):
            move = game._human_move()
            assert move == 0

    def test_human_move_rejects_invalid_number(self):
        game = Game()
        with (patch('builtins.input', side_effect=['10', '-1', '1']),
              patch('builtins.print') as mock_print):
            move = game._human_move()
            assert move == 0
            assert mock_print.call_count == 2

    def test_human_move_rejects_non_numeric_input(self):
        game = Game()
        with (patch('builtins.input', side_effect=['abc', 'x', '1']),
              patch('builtins.print') as mock_print):
            move = game._human_move()
            assert move == 0
            assert mock_print.call_count == 2

    def test_human_move_rejects_already_taken_position(self):
        game = Game()
        game.board.make_move(0, Board.PLAYER_X)
        with (patch('builtins.input', side_effect=['1', '2']),
              patch('builtins.print') as mock_print):
            move = game._human_move()
            assert move == 1
            mock_print.assert_called_with("Invalid move. Try again.")


class TestPlay:
    def test_play_alternates_between_players(self):
        game = Game()
        with (patch('builtins.input', side_effect=['1', '4', '2', '5', '3']),
              patch('game.render_board'),
              patch('builtins.print')):
            game.play()

            assert game.board.cells[0] == Board.PLAYER_X
            assert game.board.cells[3] == Board.PLAYER_O
            assert game.board.cells[1] == Board.PLAYER_X
            assert game.board.cells[4] == Board.PLAYER_O
            assert game.board.cells[2] == Board.PLAYER_X

    def test_play_renders_board_each_turn(self):
        game = Game()
        with (patch('builtins.input', side_effect=['1', '4', '2', '5', '3']),
              patch('game.render_board') as mock_render,
              patch('builtins.print')):
            game.play()

            assert mock_render.call_count == 6

    def test_play_displays_winner_when_x_wins(self):
        game = Game()
        with (patch('builtins.input', side_effect=['1', '4', '2', '5', '3']),
              patch('game.render_board'),
              patch('builtins.print') as mock_print):
            game.play()

            mock_print.assert_called_with("Winner: X")

    def test_play_displays_winner_when_o_wins(self):
        game = Game()
        with (patch('builtins.input', side_effect=['4', '1', '5', '2', '7', '3']),
              patch('game.render_board'),
              patch('builtins.print') as mock_print):
            game.play()

            mock_print.assert_called_with("Winner: O")

    def test_play_displays_draw_when_board_full(self):
        game = Game()
        moves = ['1', '3', '2', '4', '6', '5', '7', '9', '8']
        with (patch('builtins.input', side_effect=moves),
              patch('game.render_board'),
              patch('builtins.print') as mock_print):
            game.play()

            mock_print.assert_called_with("Winner: Draw")

    def test_play_ends_when_game_is_over(self):
        game = Game()
        with (patch('builtins.input', side_effect=['1', '4', '2', '5', '3']),
              patch('game.render_board'),
              patch('builtins.print')):
            game.play()

            assert game.board.is_end_state()

    def test_play_calls_human_move_for_each_turn(self):
        game = Game()
        with (patch.object(game, '_human_move', side_effect=[0, 3, 1, 4, 2]) as mock_human_move,
              patch('game.render_board'),
              patch('builtins.print')):
            game.play()

            assert mock_human_move.call_count == 5

