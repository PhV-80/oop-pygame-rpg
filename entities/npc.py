import pygame

from config import *
from entities.entity import Entity

class NPC(Entity):
    def __init__(self, x: int, y: int, width: int, height: int, color):
        super().__init__(x, y, width, height, color)
        self.speed = 3
        self.health = 100

    def update(self):
        pass