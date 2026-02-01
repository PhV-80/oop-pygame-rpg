import pygame
from config import config
from entities.character import Character
from entities.npc import NPC

# Initialize Pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((config.get_window_width(), config.get_window_height()))
pygame.display.set_caption("OOP PyGame RPG")

# Create clock for FPS
clock = pygame.time.Clock()

# Create font for UI (before game loop)
font = pygame.font.Font(None, 36)

# Create player
player = Character(50, 50, 50, 50, config.get_color_green())

# Create NPCs
npc1 = NPC(300, 200, 50, 50, config.get_color_red())
npc2 = NPC(500, 400, 50, 50, config.get_color_red())

# Game loop
running = True
game_over = False

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Update entities
        player.update()
        npc1.update(player.get_x(), player.get_y())
        npc2.update(player.get_x(), player.get_y())

        # Check collisions (using getter methods)
        if player.check_collision(npc1) or player.check_collision(npc2):
            game_over = True
            print("GAME OVER - Enemy caught you!")

    # Render frame
    screen.fill(config.get_color_black())

    if not game_over:
        player.draw(screen)
        npc1.draw(screen)
        npc2.draw(screen)

        # UI: Health display (using getter method)
        health_text = font.render(f"HP: {player.get_health()}", True, config.get_color_white())
        screen.blit(health_text, (10, 10))
    else:
        # Game Over screen
        game_over_text = font.render("GAME OVER", True, config.get_color_white())
        text_rect = game_over_text.get_rect(center=(config.get_window_width() // 2, config.get_window_height() // 2))
        screen.blit(game_over_text, text_rect)

    pygame.display.flip()
    clock.tick(config.get_fps())

pygame.quit()