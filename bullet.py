""" Contains parameters of bullet """
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Represents ship bullet """
    def __init__(self, ai_settings, screen, ship):
        """ Creates bullet in current ship position """
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self._y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self, *args):
        """ Move bullet up to the top of screen """
        self._y -= self.speed_factor
        self.rect.y = self._y

    def draw_bullet(self):
        """ Render bullet on the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
