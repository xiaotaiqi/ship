import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.OUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT
            ship.rect.centerx += 1
            
def update_screen(ai_settings,screen,ship):
    scrren.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
