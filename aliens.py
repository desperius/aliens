""" Maim module """

import sys
import pygame

def run_game():
    """ Starts main loop """
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Alien Pie :)')

    bg_color = (0, 255, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Swap buffers
        screen.fill(bg_color)
        pygame.display.flip()


run_game()
