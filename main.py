import pygame
import sys

from config import *
from entities.entity import Entity

# PyGame init
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("OOP PyGame RPG")
clock = pygame.time.Clock()

# Player create (green rect, starting in the Middle)
player = Entity(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 40, 40, COLOR_PLAYER)

# Game-Loop
running = True
while running:
    clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    player.update()

    # Draw
    screen.fill(COLOR_BG)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()