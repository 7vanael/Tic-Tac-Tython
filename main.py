from board import Board
from console import CliNotifier
from game import Game
from player_factory import PlayerFactory


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
