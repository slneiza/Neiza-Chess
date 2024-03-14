"""
gui for ma chess board
"""
import pygame
from chess import GameState
import math
import click
import sys



WIDTH = HEIGHT = 512 #am going to change once we have a sidebar to show off game info
DIMENSION = 8 # global variable for the dimension of the board
SQ_SIZE = HEIGHT // DIMENSION # size of each square on the board
IMAGES = {}
MAX_FPS = 15

'''
initialize a global dictionary of images. Will only be called once for efficiency
'''
def load_images():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


# class ChessGUI:
#     """
#     class to represent my chess graphical user interface
#     """

#     def __init__(self, window, dimension, multiplayer, game_state) -> None:
        
#         self.window = window
#         self.dimension = dimension
#         self.multiplayer = False

#         # create instance of game state
#         self.game_state = GameState()

#         #initialize pygame
#         pygame.init()

#         pygame.display.set_caption("neiza_chess")

#         self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

#         self.clock = pygame.time.Clock()

#         self.event_loop()


#     def draw_window(self) -> None:
#         """
#         Draws the contents of the window

#         Parameters: none beyond self

#         Returns: nothing
#         """

#         self.surface.fill(pygame.Color("white"))
        
#         self.draw_board(self)
#         self.draw_pieces(self)


#     def draw_board(self):
#         '''
#         Draw squares on the board
#         '''
#         colors = [pygame.Color("white"), pygame.Color("gray")]
#         for row in range(DIMENSION):
#             for col in range(DIMENSION):
#                 color = colors[((row + col) % 2)]
#                 pygame.draw.rect(self.surface, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    
#     def draw_pieces(self):
#         '''
#         draw pieces on the board
#         '''
#         for row in range(DIMENSION):
#             for col in range(DIMENSION):
#                 piece = self.game_state.board[row][col]
#                 if piece != "--": #not an empty square
#                     self.surface.blit(IMAGES[piece], pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


#     def event_loop(self) -> None:
#         """
#         Handles user interactions

#         Parameters: none beyond self

#         Returns: nothing
#         """
#         side = self.side
#         spacing = self.window/side
        

#         while running: #running the function
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#             self.draw_game(self.surface, self.game_state) #drawing the state of the game
#             self.clock.tick(MAX_FPS)
#             pygame.display.flip()

# @click.command()
# @click.option('-n', '--num-players', type=int, default=2, help='Number of players')
# @click.option('-s', '--board-size', type=int, default=8, help='Board size')
# @click.option('--othello/--non-othello', default=True, help='Game mode')
# def play_game(num_players, board_size, othello):
#     if (num_players % 2 == 1 and board_size % 2 == 0) or (num_players % 2 == 0 and board_size % 2 == 1):
#         print('Invalid combination of players and board size.')
#     neiza_chess = ChessGUI(window = 600, side_len = 100, chess = GameState)

    
    


# if __name__ == "__main__":
#     play_game()











'''
main func to run the gui. Will handle mouse clicks
'''
def main():
    pygame.init()
    pygame.display.set_caption("neiza_chess")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = GameState() 
    load_images() #only do this once
    running = True

    while running: #running the function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_game(screen, game_state) #drawing the state of the game
        clock.tick(MAX_FPS)
        pygame.display.flip()

'''
function that draws the game on the board
'''
def draw_game(screen, game_state):
    draw_board(screen) #draw squares on the board
    #add piece highlighting or move suggestions later
    draw_pieces(screen, game_state.board) #draw pieces on top of the board 


'''
Draw squares on the board
'''
def draw_board(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


     
'''
draw pieces on the board
'''
def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--": #not an empty square
                screen.blit(IMAGES[piece], pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))




if __name__ == "__main__":
    main()


    

    

