from board import Board
from console import render_welcome, render_board

def main():
    render_welcome()
    board = Board()
    render_board(board)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
