import pygame
import sys

# Initialize PyGame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shadow Chaser - Level 1")

# Colors
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 100)

# Player settings
player_pos = [1, 1]  # Grid position
player_radius = 15
light_radius = 120  # Visible radius around player
player_speed = 5

# Maze (0 = empty, 1 = wall, 2 = exit)
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,2,1],
    [1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1],
    [1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1],
    [1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1],
    [1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

ROWS = len(maze)
COLS = len(maze[0])

def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            tile = maze[row][col]
            x, y = col * TILE_SIZE, row * TILE_SIZE
            if tile == 1:
                pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 2:
                pygame.draw.rect(screen, GREEN, (x, y, TILE_SIZE, TILE_SIZE))

def get_rect(row, col):
    return pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_UP]:
        dy = -player_speed
    if keys[pygame.K_DOWN]:
        dy = player_speed
    if keys[pygame.K_LEFT]:
        dx = -player_speed
    if keys[pygame.K_RIGHT]:
        dx = player_speed

    # Calculate new position
    new_x = player_pos[0] * TILE_SIZE + dx
    new_y = player_pos[1] * TILE_SIZE + dy

    # Player rect
    player_rect = pygame.Rect(new_x, new_y, player_radius*2, player_radius*2)

    # Collision check with walls
    collided = False
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                if player_rect.colliderect(get_rect(row, col)):
                    collided = True

    if not collided:
        player_pos[0] += dx / TILE_SIZE
        player_pos[1] += dy / TILE_SIZE

    # Draw maze
    screen.fill(BLACK)
    draw_maze()

    # Player position in pixels
    px = int(player_pos[0] * TILE_SIZE + TILE_SIZE // 2)
    py = int(player_pos[1] * TILE_SIZE + TILE_SIZE // 2)

    # Draw player
    pygame.draw.circle(screen, YELLOW, (px, py), player_radius)

    # Darkness mask
    darkness = pygame.Surface((WIDTH, HEIGHT))
    darkness.fill(BLACK)
    pygame.draw.circle(darkness, (0, 0, 0, 0), (px, py), light_radius)
    darkness.set_colorkey((0, 0, 0))
    screen.blit(darkness, (0, 0))

    # Check exit
    if maze[int(player_pos[1])][int(player_pos[0])] == 2:
        print("Level Complete!")
        running = False

    # Update display
    pygame.display.flip()
