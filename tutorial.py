import pygame
from index import draw

width, height = 700, 500
window = pygame.display.set_mode((width, height))

game = Game(window, width, height)

run = True
while run:
    game.loop()
    game.draw()
    pygame.display.update()