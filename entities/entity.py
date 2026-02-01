import pygame

from config import *

class Entity:
    """Base-Class for all Gameobjects (Player, NPCs, etc.)"""

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, int, int], health: int, alive: bool):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
        self.__health = health
        self.__alive = alive

        self.set_x(width)
        self.set_y(height)
        self.set_color(color)
        self.set_health(health)
        self.set_alive(alive)

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def get_color(self) -> tuple[int, int, int]:
        return self.__color

    def get_health(self) -> int:
        return self.__health

    def get_alive(self) -> bool:
        return self.__alive

    def set_x(self, value: int):
        if 0 <= value <= WINDOW_WIDTH - self.__width:
            self.__x = value

    def set_y(self, value: int):
        if 0 <= value <= WINDOW_WIDTH - self.__width:
            self.__y = value

    def set_width(self, value: int):
        self.__width = value

    def set_height(self, value: int):
        self.__height = value

    def set_color(self, value: tuple[int, int, int]):
        self.__color = value

    def set_health(self, value: int):
        self.__health = value

    def set_alive(self, value: bool):
        self.__alive = value

    def update(self):
        """Call every Frame. Override for custom logic."""
        pass

    def draw(self, screen):
        """Draws Entity as Rect."""
        pygame.draw.rect(screen, self.set_color(), (self.x, self.y, self.width, self.height))

    def get_rect(self):
        """Returns a rectangle for collision checks."""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision(self, other):
        """Checks whether this entity collides with another."""
        return self.get_rect().colliderect(other.get_rect())

    def take_damage(self, amount):
        self.health