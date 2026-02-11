import random
from .npc import NPC
from config import config

class WanderNPC(NPC):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.change_timer = 0
        self.direction_x = random.choice([-1, 0, 1])
        self.direction_y = random.choice([-1, 0, 1])
        self.change_timer = 0
        self.change_interval = 120

    def get_direction_x(self) -> int:
        return self.direction_x

    def get_direction_y(self) -> int:
        return self.direction_y

    def set_direction_x(self, new_x):
        self.direction_x = new_x

    def set_direction_y(self, new_y):
        self.direction_y = new_y

    def update(self):
        self.change_timer += 1

        # actual not moving!!!
        if self.change_timer >= self.change_interval:
            self.direction_x = random.choice([-1, 0, 1])
            self.direction_y = random.choice([-1, 0, 1])
            self.change_timer = 0

        self.set_x(new_x)
        self.set_y(new_y)

        if new_x > self.get_x():
            new_x = new_x - self.get_x()

        if new_y > self.get_y():
            new_y = new_y - self.get_y()

        if new_x < self.get_x():
            new_x = new_x + self.get_x()

        if new_y < self.get_y():
            new_y = new_y + self.get_y()

        self.x = new_x
        self.y = new_y

        self.clamp_to_bounds()