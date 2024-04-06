import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 5  
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = (1, 0)  # Initial direction: moving right
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

game_over = False

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def handle_input():
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

def move_snake():
    global snake, food, game_over

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if new_head[0] < 0:
        new_head = (GRID_WIDTH - 1, new_head[1])
    elif new_head[0] >= GRID_WIDTH:
        new_head = (0, new_head[1])
    elif new_head[1] < 0:
        new_head = (new_head[0], GRID_HEIGHT - 1)
    elif new_head[1] >= GRID_HEIGHT:
        new_head = (new_head[0], 0)

    if new_head in snake[1:]:
        game_over = True
        return

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

while not game_over:
    handle_input()

    move_snake()

    screen.fill(BLACK)

    draw_snake()
    draw_food()

    pygame.display.flip()

    
    clock.tick(FPS)


font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over!", True, WHITE)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()


pygame.time.wait(2000)
pygame.quit()
quit()