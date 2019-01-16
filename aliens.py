""" Maim module """

import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    """ Starts main loop """
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption('Alien Pie :)')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Swap buffers
        pygame.display.flip()


run_game()
