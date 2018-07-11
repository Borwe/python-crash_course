import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    a1_settings=Settings()
    screen=pygame.display\
        .set_mode((a1_settings.screen_width,a1_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make Ship
    ship=Ship(screen)

    # start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events()

        gf.update_screen(a1_settings,screen,ship)

run_game()
