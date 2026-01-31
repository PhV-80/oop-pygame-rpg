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

font = pygame.font.Font(None, 36)

# Create player character (green rectangle, spawns at window center)
player = Character(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 40, 40, COLOR_PLAYER)

# Create NPCs (red rectangles, will chase player)
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
    npc1.update(player.x, player.y)
    npc2.update(player.x, player.y)

    npcs = [npc1, npc2]

    # Check for collisions between player and NPCs (game over condition)
    for npc in npcs:
        if player.check_collision(npc):
            print("Game Over! You were caught by an enemy!")
            running = False
            break

    # Render frame
    screen.fill(COLOR_BG)
    player.draw(screen)
    npc1.draw(screen)
    npc2.draw(screen)

    text_surface = font.render(f"HP: {player.health}", True, COLOR_WHITE)
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()  # Update display

# Cleanup
pygame.quit()
sys.exit()