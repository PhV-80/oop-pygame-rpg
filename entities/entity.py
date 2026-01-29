import pygame

class Entity:
    """ Base-Class for all Gameobjects (Player, NPCs, etc.) """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def update(self):
        """ Call every Frame. Override for custom logic. """
        pass

    def draw(self, screen):
        """ Draws Entity as Rect. """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        """ Returns a rectangle for collision checks. """
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision(self, other):
        """ Checks whether this entity conflicts with another. """
        return self.get_rect().colliderect(other.get_rect())