""" Class for ship """

import pygame

class Ship():
    """ Class for ship """
    def __init__(self, screen):
        """ Initialize ship and its settings """
        # Load image and get rect
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ Render ship """
        self.screen.blit(self.image, self.rect)
        