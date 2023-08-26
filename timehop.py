# Importing required libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = 50
BLOCK_SIZE = 50
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Time-Hop Prototype")
clock = pygame.time.Clock()

# Initialize variables
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * PLAYER_SIZE]
time_epoch = 0  # 0 for past, 1 for future
blocks = []  # Blocks for the player to avoid

# Generate initial blocks
for i in range(10):
    block_x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
    block_y = random.randint(0, SCREEN_HEIGHT - 2 * BLOCK_SIZE)
    blocks.append([block_x, block_y, time_epoch])  # x, y, time_epoch

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_SPACE]:
        time_epoch = 1 - time_epoch  # Switch time epoch

    # Draw background
    screen.fill(WHITE if time_epoch == 0 else BLACK)

    # Draw player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    # Draw blocks
    for block in blocks:
        if block[2] == time_epoch:
            pygame.draw.rect(screen, BLUE, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
