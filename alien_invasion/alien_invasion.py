import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    a1_settings=Settings()
    screen=pygame.display\
        .set_mode((a1_settings.screen_width,a1_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make Ship
    ship=Ship(a1_settings,screen)

    # Mage a group to store bullets in.
    bullets=Group()

    # start the main loop for the game
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(a1_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(a1_settings,screen,ship,bullets)

run_game()
