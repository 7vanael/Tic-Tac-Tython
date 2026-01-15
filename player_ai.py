import math
from board import Board
from player import Player


class HardAI(Player):
    def __init__(self, character: str, notifier):
        super().__init__(character, notifier)
        self.opponent_character = (
            Board.PLAYER_O if character == Board.PLAYER_X else Board.PLAYER_X
        )

    def select_move(self, board: Board) -> int:
        best_score = -math.inf
        move = None

        for possible_move in board.available_moves():
            board.make_move(possible_move, self.character)
            score = self.minimax(board, depth=0, is_maximizing=False)
            board.clear_cell(possible_move)

            if score > best_score:
                best_score = score
                move = possible_move
        self.notifier.announce_move(self.character, move)
        return move

    def minimax(self, board: Board, depth: int, is_maximizing: bool):
        if board.is_end_state():
            return self.calculate_terminal_score(board, depth)

        if is_maximizing:
            best_score = -math.inf
            for possible_move in board.available_moves():
                board.make_move(possible_move, self.character)
                score = self.minimax(board, depth + 1, is_maximizing=False)
                board.clear_cell(possible_move)
                best_score = max(best_score, score)
            return best_score

        else:
            best_score = math.inf
            for possible_move in board.available_moves():
                board.make_move(possible_move, self.opponent_character)
                score = self.minimax(board, depth + 1, is_maximizing=True)
                board.clear_cell(possible_move)
                best_score = min(best_score, score)
            return best_score

    def calculate_terminal_score(self, board: Board, depth: int) -> int:
        winner = board.winner()
        if winner == self.character:
            return 10 - depth
        elif winner == self.opponent_character:
            return depth - 10
        else:
            return 0