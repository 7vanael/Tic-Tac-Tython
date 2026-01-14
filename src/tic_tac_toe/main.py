from tic_tac_toe.board import Board
from tic_tac_toe.console import CliNotifier
from tic_tac_toe.game import Game
from tic_tac_toe.player.ai_player import HardAI
from tic_tac_toe.player.human_player import HumanPlayer


def main():
    notifier = CliNotifier()
    notifier.render_welcome()
    board = Board()
    players = {
        Board.PLAYER_X: HumanPlayer(Board.PLAYER_X),
        Board.PLAYER_O: HardAI(Board.PLAYER_O),
    }
    game = Game(board, players, notifier)
    game.play()

if __name__ == '__main__':
    main()
