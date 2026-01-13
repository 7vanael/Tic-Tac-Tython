from tic_tac_toe.console import render_welcome
from tic_tac_toe.game import Game


def main():
    render_welcome()
    game = Game()
    game.play()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
