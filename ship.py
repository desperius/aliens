""" Class for ship """

import pygame

class Ship():
    """ Class for ship """
    def __init__(self, ai_settings, screen):
        """ Initialize ship and its settings """
        # Load image and get rect
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update ship position """
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and (self.rect.left > self.screen_rect.left):
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """ Render ship """
        self.screen.blit(self.image, self.rect)
        