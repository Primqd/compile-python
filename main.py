import pygame
from pygame.locals import *
from sys import exit

from card import Card

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
pygame.time.Clock().tick(FPS)

# Global Colors
WHITE = (255, 255, 255)

# https://www.reddit.com/r/midjourney/comments/10vbtri/aspect_ratio_of_standard_playing_cards/
card = Card(150,150,63,88)

# game loop
while True:
    DISPLAY.fill(WHITE) # needed, display not cleared by default

    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        card.handle_event(event)

    card.draw(DISPLAY)
    pygame.display.update()