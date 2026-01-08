import pygame
from pygame.locals import *
from sys import exit

pygame.init()

DISPLAY = pygame.display.set_mode((300,300))

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()