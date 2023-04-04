import pygame
import random
from player import *
from enemy import *
from debug import *

# initialize pygame
pygame.init()

# set up the game window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chrono Detective Star")

# set up the game clock
clock = pygame.time.Clock()

# define game variables
running = True

# Create player instance
player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites = pygame.sprite.Group()
debug_sprite = pygame.sprite.Group()
all_sprites.add(player)

# Create enemy instances
num_enemies = 5
enemies = pygame.sprite.Group()
for i in range(num_enemies):
    enemy = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    all_sprites.add(enemy)
    enemies.add(enemy)

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or player.health <0:
            running = False
    screen.fill((0, 0, 0))
    debug((player.health, player.score))
    # Update all sprites
    player_pos = pygame.math.Vector2(player.rect.center)
    all_sprites.update(player_pos)

    # Check for collisions between player and enemies
    if pygame.sprite.spritecollide(player, enemies, True):
        player.health -= 10

    # Draw all sprites
    all_sprites.draw(screen)
    debug_sprite.draw(screen)

    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# exit game
pygame.quit()
