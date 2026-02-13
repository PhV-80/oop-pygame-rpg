from .character import Character


class Player(Character):
    def __init__(self, width: int = 50, height: int = 50, color: tuple = (0, 255, 0)):
        super().__init__(width, height, color)
