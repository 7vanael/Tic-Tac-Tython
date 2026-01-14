from typing import List


def render_welcome():
    print('Welcome to Tic-Tac-Tython!\n Let\'s play!')

def interleave_numbers(cells) ->List[str]:
    return [str(i + 1) if c == " " else c for i, c in enumerate(cells)]

def render_board(board):
    display = interleave_numbers(board.cells)
    for i in range(0, 9, 3):
        print(" | ".join(display[i:i + 3]))
        if i < 6:
            print("---------")
    print()