"""""
chess implimentation, boutta create my own version of chess
"""

class GameState():
    def __init__(self) -> None:
        # board is an 8x8 2d list
        # each elemetn has 2 characters, 
        # first character represents color of the piece
        # second character represents piece itself
        # "--" representes empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]            
        ]
        self.white_to_move = True
        self.recent_moves = []




