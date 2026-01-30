import pygame

from config import *
from entities.entity import Entity

class Character(Entity):
    def __init__(self, x: int, y: int, width: int, height: int, color):
        super().__init__(x, y, width, height, color)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        while keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed

        while keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed

        while keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed

        while keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed

        if self.x < 0 or self.x > WINDOW_WIDTH - self.width:
            self.x = WINDOW_WIDTH - self.width

        if self.y < 0 or self.y > WINDOW_HEIGHT - self.height:
            self.y = WINDOW_HEIGHT - self.height