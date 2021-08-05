import pygame

class Fox:
    """A class to manage the fox."""

    def __init__(self, f_game):
        """Initialize the ship and set its starting position."""
        self.screen = f_game.screen
        self.screen_rect = f_game.screen.get_rect()

        # Load the fox image and get its rect.
        self.image = pygame.image.load('images/fox.bmp')
        self.rect = self.image.get_rect()
        # Start each new fox at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the fox at its current location."""
        self.screen.blit(self.image, self.rect)