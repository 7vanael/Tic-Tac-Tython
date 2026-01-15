from board import Board
from player_ai import HardAI
from player_human import HumanPlayer


class PlayerFactory:
    PLAYER_TYPES = {
        "Human": HumanPlayer,
        "Hard AI": HardAI,
    }

    def __init__(self, notifier):
        self.notifier = notifier

    def create_players(self):
        x_type = self.notifier.select_player_type(Board.PLAYER_X, self.PLAYER_TYPES)
        o_type = self.notifier.select_player_type(Board.PLAYER_O, self.PLAYER_TYPES)
        return {
            Board.PLAYER_X: self._create_player(Board.PLAYER_X, x_type),
            Board.PLAYER_O: self._create_player(Board.PLAYER_O, o_type)
        }

    def _create_player(self, symbol, player_type):
        try:
            player_class = self.PLAYER_TYPES[player_type]
        except KeyError:
            raise ValueError(f"Unknown player type: {player_type}")

        return player_class(symbol, self.notifier)