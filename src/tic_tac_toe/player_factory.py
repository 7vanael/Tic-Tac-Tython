from tic_tac_toe.board import Board
from tic_tac_toe.player.ai_player import HardAI
from tic_tac_toe.player.human_player import HumanPlayer


class PlayerFactory:
    PLAYER_TYPES = {
        "human": {
            "label": "Human",
            "class": HumanPlayer,
        },
        "ai_hard": {
            "label": "Hard AI",
            "class": HardAI,
        },
        # "ai_easy": {
        #     "label": "Easy AI",
        #     "class": EasyAI,
        # },
    }


    def __init__(self, notifier):
        self.notifier = notifier

    def create_players(self):
        options = self.get_player_type_options()
        x_type = self.notifier.select_player_type(Board.PLAYER_X, options)
        o_type = self.notifier.select_player_type(Board.PLAYER_O, options)
        return {
            Board.PLAYER_X: self._create_player(Board.PLAYER_X, x_type),
            Board.PLAYER_O: self._create_player(Board.PLAYER_O, o_type)
        }

    def _create_player(self, symbol, player_type):
        try:
            player_class = self.PLAYER_TYPES[player_type]["class"]
        except KeyError:
            raise ValueError(f"Unknown player type: {player_type}")

        return player_class(symbol)

    def get_player_type_options(self):
        return {
            key: info["label"]
            for key, info in self.PLAYER_TYPES.items()
        }