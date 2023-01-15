import pygame
import sys
import numpy as np

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
box_size = 25

BLACK = (0, 0, 0)
GRAY = (48, 48, 48)
GREEN = (0, 224, 0)


def main():
    # INITIALIZE THE GAME
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Gra w życie')

    # CLOCK
    FPS = 5
    clock = pygame.time.Clock()

    screen.fill(GRAY)
    grid = np.zeros((WINDOW_WIDTH // box_size, WINDOW_HEIGHT // box_size))
    pause_game = False

    while True:
        drawGrid(grid, box_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                button_number = event.button
                button_position_x, button_position_y = event.pos
                if button_number == 1:
                    if grid[button_position_x // box_size][button_position_y // box_size] == 0:
                        grid[button_position_x // box_size][button_position_y // box_size] = 1
                        pygame.display.update()
                    else:
                        grid[button_position_x // box_size][button_position_y // box_size] = 0
                        pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:  # Zamykanie gry
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:  # Wstrzymywanie animacji
                    if pause_game:
                        pause_game = False
                    else:
                        pause_game = True
                elif event.key == pygame.K_EQUALS:  # Przyspieszanie animacji
                    FPS += 1
                elif event.key == pygame.K_MINUS:  # Spowalnianie animacji
                    if FPS > 1:
                        FPS -= 1
                elif event.key == pygame.K_c:  # Resetowanie gry
                    grid = np.zeros((WINDOW_WIDTH // box_size, WINDOW_HEIGHT // box_size))

        if not pause_game:
            grid = life(grid)

        pygame.display.update()
        clock.tick(FPS)


def drawGrid(grid, boxSize):
    for x in range(0, len(grid)):
        for y in range(0, grid.size // len(grid)):
            if grid[x][y] == 0:
                # DRAW A BLACK SQUARE
                rect = pygame.Rect(x * boxSize, y * boxSize, boxSize - 1, boxSize - 1)
                pygame.draw.rect(screen, BLACK, rect)
            else:
                # DRAW A GREEN SQUARE
                rect = pygame.Rect(x * boxSize, y * boxSize, boxSize - 1, boxSize - 1)
                pygame.draw.rect(screen, GREEN, rect)


def count_neighbors(grid, x, y):
    neighbors = 0
    for p in range(x - 1, x + 2):
        for q in range(y - 1, y + 2):
            if not (p == x and q == y):
                if 0 <= p < len(grid) and 0 <= q < (grid.size // len(grid)):
                    if grid[p][q] == 1:
                        neighbors += 1
    return neighbors


def life(grid):
    next_generation = np.zeros((WINDOW_WIDTH // box_size, WINDOW_HEIGHT // box_size))
    for x in range(0, len(grid)):
        for y in range(0, grid.size // len(grid)):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 0:  # Komórka jest martwa
                if neighbors == 3:
                    next_generation[x][y] = 1
            else:
                if neighbors == 2 or neighbors == 3:
                    next_generation[x][y] = 1
    return next_generation


if __name__ == "__main__":
    main()