from tic_tac_toe.board import Board
from tic_tac_toe.console import CliNotifier
from tic_tac_toe.game import Game
from tic_tac_toe.player_factory import PlayerFactory


def main():
    notifier = CliNotifier()
    notifier.render_welcome()
    board = Board()
    player_factory = PlayerFactory(notifier)
    players = player_factory.create_players()
    game = Game(board, players, notifier)
    game.play()

if __name__ == '__main__':
    main()
