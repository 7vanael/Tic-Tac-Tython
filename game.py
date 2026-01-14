from board import Board
from console import render_board

class Game:
    def __init__(self):
        self.board = Board()

    def play(self):
        current_player = Board.PLAYER_X

        while not self.board.is_end_state():
            render_board(self.board)
            move = self._human_move()
            # hvh to start... eyes on alternating next
            # if current_player == Board.PLAYER_X:
            #     move = self._human_move()
            # else:
            #     move = computer_move(self.board)

            self.board.make_move(move, current_player)
            current_player = (
                Board.PLAYER_O if current_player == Board.PLAYER_X else Board.PLAYER_X
            )

        render_board(self.board)
        winner = self.board.winner()
        print(f"Winner: {winner if winner else 'Draw'}")

    def _human_move(self) -> int:
        while True:
            try:
                move = int(input("Choose a move (1-9): ")) - 1
                if move in self.board.available_moves():
                    return move
            except ValueError:
                pass
            print("Invalid move. Try again.")

