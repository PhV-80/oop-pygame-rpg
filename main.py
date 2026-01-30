import pygame
import sys

from config import *
from entities.character import Character
from entities.npc import NPC

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("OOP PyGame RPG")
clock = pygame.time.Clock()

# Create player character (green rectangle, spawns at window center)
player = Character(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 40, 40, COLOR_PLAYER)

# Create NPCs (red rectangles, static for now)
npc1 = NPC(100, 100, 30, 30, COLOR_NPC)
npc2 = NPC(600, 400, 30, 30, COLOR_NPC)

# Main game loop
running = True
while running:
    clock.tick(FPS)  # Maintain target framerate (60 FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    player.update()
    npc1.update()
    npc2.update()

    # Render frame
    screen.fill(COLOR_BG)
    player.draw(screen)
    npc1.draw(screen)
    npc2.draw(screen)
    pygame.display.flip()  # Update display

# Cleanup
pygame.quit()
sys.exit()