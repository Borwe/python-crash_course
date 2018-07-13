import sys
import pygame
from bullet import Bullet

def check_events(a1_settings,screen,ship,bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event,a1_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event,ship)


def update_screen(a1_settings,screen,ship,bullets):
    # Redraw the screen during each pass through the loop
    screen.fill(a1_settings.bg_color)
    ship.blitme()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def check_key_down_events(event,a1_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        new_bullet=Bullet(a1_settings,screen,ship)
        bullets.add(new_bullet)


def check_key_up_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False