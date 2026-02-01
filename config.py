"""Game configuration with encapsulation."""

class Config:
    """Game configuration class with getter methods."""

    def __init__(self):
        """Initialize configuration values."""
        self.window_width = 800
        self.window_height = 600
        self.fps = 60
        self.color_black = (0, 0, 0)
        self.color_white = (255, 255, 255)
        self.color_red = (255, 0, 0)
        self.color_green = (0, 255, 0)

    # Getter methods for window settings
    def get_window_width(self) -> int:
        """Get window width in pixels."""
        return self.window_width

    def get_window_height(self) -> int:
        """Get window height in pixels."""
        return self.window_height

    def get_fps(self) -> int:
        """Get frames per second limit."""
        return self.fps

    # Getter methods for colors
    def get_color_black(self) -> tuple:
        """Get black color RGB tuple."""
        return self.color_black

    def get_color_white(self) -> tuple:
        """Get white color RGB tuple."""
        return self.color_white

    def get_color_red(self) -> tuple:
        """Get red color RGB tuple."""
        return self.color_red

    def get_color_green(self) -> tuple:
        """Get green color RGB tuple."""
        return self.color_green


# Singleton instance
config = Config()