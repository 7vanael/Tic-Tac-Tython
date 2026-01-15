from tic_tac_toe.board import Board
from tic_tac_toe.player.player import Player
from tic_tac_toe.console import CliNotifier

class Game:
    def __init__(self, board: Board, players: dict[str, Player], notifier: CliNotifier):
        self.board = board
        self.players = players
        self.current_player = Board.PLAYER_X
        self.notifier = notifier

    def play(self):
        while not self.board.is_end_state():
            self.notifier.render_board(self.board)
            player = self.players[self.current_player]
            move = player.select_move(self.board)
            self.board.make_move(move, self.current_player)
            self.current_player = (
                Board.PLAYER_O if self.current_player == Board.PLAYER_X else Board.PLAYER_X
            )

        self.notifier.render_board(self.board)
        winner = self.board.winner()
        self.notifier.notify_winner(winner)
