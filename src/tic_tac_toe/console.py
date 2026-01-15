from typing import List

class CliNotifier:
    @staticmethod
    def render_welcome():
        print('Welcome to Tic-Tac-Tython!\n Let\'s play!')

    def select_player_type(self, symbol: str, options: dict[str, type]) -> str:
        keys = list(options.keys())
        while True:
            self._display_player_options(keys, symbol)
            print(f"Enter selection: ", end="")
            try:
                index = int(input()) - 1
                if 0 <= index < len(keys):
                    return keys[index]
            except ValueError:
                pass

            print(f"Invalid choice. Please enter a number between 1 and {len(keys)}.")

    @staticmethod
    def _display_player_options(keys: list, symbol: str):
        print(f"Enter a number to select player type for {symbol}:")
        for i, key in enumerate(keys, start=1):
            print(f"{i}. {key}")

    @staticmethod
    def _interleave_numbers(cells) ->List[str]:
        return [str(i + 1) if c == " " else c for i, c in enumerate(cells)]

    def render_board(self, board):
        display = self._interleave_numbers(board.cells)
        for i in range(0, 9, 3):
            print(" | ".join(display[i:i + 3]))
            if i < 6:
                print("---------")
        print()

    @staticmethod
    def notify_winner(winner: str | None):
        if winner:
            print(f"Winner: {winner}")
        else:
            print("Draw!")