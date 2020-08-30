import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.OUIT:
            sys.exit()
            
def uplate_screen(ai_settings,screen,ship):
    scrren.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
