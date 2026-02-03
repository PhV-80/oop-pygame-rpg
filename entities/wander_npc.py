import random
from entities.npc import NPC
from config import config

class WanderNPC(NPC):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        super().__init__(x, y, width, height, color)
        self.change_timer = 0
        self.direction_x = random.choice([-1, 0, 1])
        self.direction_y = random.choice([-1, 0, 1])
        self.change_timer = 0
        self.change_interval = 120

    def update(self):
        self.change_timer += 1

        # actual not moving!!!
        if self.change_timer >= self.change_interval:
            self.direction_x = random.choice([-1, 0, 1])
            self.direction_y = random.choice([-1, 0, 1])
            self.change_timer = 0
