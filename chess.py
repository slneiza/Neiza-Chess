import math
import click
import sys
from typing import List, Tuple
import click



"""""
chess implimentation, boutta create my own version of chess
"""


DIMENSION = 8 # global variable for the dimension of the board

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
    
    def make_move(self, piece: str, desired_position: tuple, current_pos: tuple)->None:
        '''
        makes a move with a piece and position as arguments, for now moves dont
        have to be legal. 
        '''
        desired_row = desired_position[0]
        desired_col = desired_position[1]
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                if self.board[desired_row][desired_col] == "--":
                    self.board[desired_row][desired_col] = piece
                    self.board[current_pos[0]][current_pos[1]] = "--"
    def print_board(self)->str:
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                print(self.board[row][col])




