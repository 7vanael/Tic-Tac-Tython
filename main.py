from console import render_welcome
from game import Game


def main():
    render_welcome()
    game = Game()
    game.play()

if __name__ == '__main__':
    main()
