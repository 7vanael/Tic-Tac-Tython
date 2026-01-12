import math

from board import Board

class HardAI:
    def __init__(self, ai_character: str):
        self.ai_character = ai_character
        self.opponent_character = (
            Board.PLAYER_O if ai_character == Board.PLAYER_X else Board.PLAYER_X
        )

    def best_move(self, board: Board):
        best_score = -math.inf
        move = None

        for possible_move in board.available_moves():
            board.make_move(possible_move, self.ai_character)
            score = self.minimax(board, is_maximizing=False)
            board.clear_cell(possible_move)

            if score > best_score:
                best_score = score
                move = possible_move

        return move

    def minimax(self, board: Board, is_maximizing: bool):
        winner = board.winner()
        if winner == self.ai_character:
            return 1
        if winner == self.opponent_character:
            return -1
        if board.is_full():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for possible_move in board.available_moves():
                board.make_move(possible_move, self.opponent_character)
                score = self.minimax(board, is_maximizing=False)
                board.clear_cell(possible_move)
                best_score = max(best_score, score)
            return best_score

        else:
            best_score = math.inf
            for possible_move in board.available_moves():
                board.make_move(possible_move, self.ai_character)
                score = self.minimax(board, is_maximizing=True)
                board.clear_cell(possible_move)
                best_score = min(best_score, score)
            return best_score