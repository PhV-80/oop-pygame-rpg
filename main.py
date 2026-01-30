import pygame
import sys

from config import *
from entities.character import Character
from entities.npc import NPC

# PyGame init
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("OOP PyGame RPG")
clock = pygame.time.Clock()

# Player create (green rect, starting in the Middle)
player = Character(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 40, 40, COLOR_PLAYER)

# NPC create (red rect)
npc1 = NPC(100, 100, 30, 30, COLOR_NPC)
npc2 = NPC(600, 400, 30, 30, COLOR_NPC)

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
    npc1.update()
    npc2.update()

    # Draw
    screen.fill(COLOR_BG)
    player.draw(screen)
    npc1.draw(screen)
    npc2.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()