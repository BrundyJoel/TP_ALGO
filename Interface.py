import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 8
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
WHITE = (240, 240, 240)
BLACK = (30, 30, 30)
RED = (220, 50, 50)
BLUE = (50, 50, 220)
HIGHLIGHT = (255, 215, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fanorona Telo")
screen.fill(WHITE)

# Grille du jeu
board = [[1, 1, 1],
         [0, 0, 0],
         [2, 2, 2]]

player_turn = 1  # 1 pour joueur 1, 2 pour joueur 2

def draw_board():
    screen.fill(WHITE)
    # Dessiner le carré extérieur
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE//2, SQUARE_SIZE//2), (WIDTH - SQUARE_SIZE//2, SQUARE_SIZE//2), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE//2, HEIGHT - SQUARE_SIZE//2), (WIDTH - SQUARE_SIZE//2, HEIGHT - SQUARE_SIZE//2), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE//2, SQUARE_SIZE//2), (SQUARE_SIZE//2, HEIGHT - SQUARE_SIZE//2), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (WIDTH - SQUARE_SIZE//2, SQUARE_SIZE//2), (WIDTH - SQUARE_SIZE//2, HEIGHT - SQUARE_SIZE//2), LINE_WIDTH)
    
    # Dessiner les lignes intérieures
    pygame.draw.line(screen, BLACK, (WIDTH//2, SQUARE_SIZE//2), (WIDTH//2, HEIGHT - SQUARE_SIZE//2), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE//2, HEIGHT//2), (WIDTH - SQUARE_SIZE//2, HEIGHT//2), LINE_WIDTH)
    
    # Dessiner les diagonales
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE//2, SQUARE_SIZE//2), (WIDTH - SQUARE_SIZE//2, HEIGHT - SQUARE_SIZE//2), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (WIDTH - SQUARE_SIZE//2, SQUARE_SIZE//2), (SQUARE_SIZE//2, HEIGHT - SQUARE_SIZE//2), LINE_WIDTH)

def draw_pieces():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (x, y), CIRCLE_RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLUE, (x, y), CIRCLE_RADIUS)

def is_valid_move(from_pos, to_pos):
    row1, col1 = from_pos
    row2, col2 = to_pos
    if board[row2][col2] == 0:
        if abs(row1 - row2) + abs(col1 - col2) == 1 or abs(row1 - row2) == abs(col1 - col2) == 1:
            return True
    return False

def move_piece(from_pos, to_pos):
    row1, col1 = from_pos
    row2, col2 = to_pos
    board[row2][col2] = board[row1][col1]
    board[row1][col1] = 0

def check_win(player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            return True
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)):
        return True
    return False

running = True
selected_piece = None
while running:
    draw_board()
    draw_pieces()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            row, col = event.pos[1] // SQUARE_SIZE, event.pos[0] // SQUARE_SIZE
            if board[row][col] == player_turn:
                selected_piece = (row, col)
                pygame.draw.circle(screen, HIGHLIGHT, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, 5)
            elif selected_piece and is_valid_move(selected_piece, (row, col)):
                move_piece(selected_piece, (row, col))
                if check_win(player_turn):
                    print(f"Joueur {player_turn} gagne!")
                    running = False
                selected_piece = None
                player_turn = 3 - player_turn
            else:
                selected_piece = None
    
    pygame.display.flip()

pygame.quit()
sys.exit()
