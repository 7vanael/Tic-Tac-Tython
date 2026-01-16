from board import Board
from console import CliNotifier
from game import Game
from player_factory import PlayerFactory


def main():
    notifier = CliNotifier()
    notifier.render_welcome()
    player_factory = PlayerFactory(notifier)
    is_playing = True
    while is_playing:
        board = Board()
        players = player_factory.create_players()
        game = Game(board, players, notifier)
        game.play()
        is_playing = notifier.play_again()

if __name__ == '__main__':
    main()
