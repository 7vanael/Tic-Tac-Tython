from typing import List
from tic_tac_toe.board import Board

class CliNotifier:
    def render_welcome(self):
        print('Welcome to Tic-Tac-Tython!\n Let\'s play!')

    def interleave_numbers(self, cells) ->List[str]:
        return [str(i + 1) if c == " " else c for i, c in enumerate(cells)]

    def render_board(self, board):
        display = self.interleave_numbers(board.cells)
        for i in range(0, 9, 3):
            print(" | ".join(display[i:i + 3]))
            if i < 6:
                print("---------")
        print()

    def notify_winner(self, winner: str | None):
        if winner:
            print(f"Winner: {winner}")
        else:
            print("Draw!")