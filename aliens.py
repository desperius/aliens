""" Maim module """

import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship

import utilities as gf

def run_game():
    """ Starts main loop """
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    pygame.display.set_caption('Alien Pie :)')

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
