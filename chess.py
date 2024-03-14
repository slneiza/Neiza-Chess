import math
import click
import sys
from typing import List, Tuple
import click



"""""
chess implimentation, boutta create my own version of chess
"""


DIMENSION = 8 # global variable for the dimension of the board
COL_DICT = {'A' : 0, 'B': 1 , 'C' : 2, 'D' : 3, 'E': 4, 'F': 5, 'G':6, 'H':7,}

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
        self.legal_moves = {'wP':[], "wR":[], "wN" :[], "wB" : [], "wQ": [], "wK": [],"bP": [], "bR":[],  "bN": [], "bB": [],  "bQ": [], "bK":[] }
    
    def make_move(self, piece: str, desired_position: str, current_pos: str)->None:
        '''
        makes a move with a piece and position as arguments, for now moves dont
        have to be legal. 
        '''
        if self.white_to_move == True:
            self.white_to_move = False
        else:
            self.white_to_move =True

        desired_col = COL_DICT[desired_position[0]]
        desired_row = DIMENSION - int(desired_position[1]) 
        current_col = COL_DICT[current_pos[0]]
        current_row = DIMENSION - int(current_pos[1])

        self.board[current_row][current_col] = "--"
        self.board[desired_row][desired_col] = piece
        self.recent_moves.append(piece[1] + desired_position)
    
    def legal_moves(self)->None:
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                piece = self.board[row][col]
        
        
        



    def print_board(self)->str:
        '''
        prints the current state of the board
        '''
        print("   A  B  C  D  E  F  G  H")
        
        row_number = 8
        for row in self.board:
            print(f"{row_number}  " + ' '.join(row))
            row_number -= 1



if __name__ == "__main__":
    game_state = GameState()
    game_state.make_move("wP", 'D4', 'D2' )
    game_state.print_board()
    print (game_state.recent_moves)





