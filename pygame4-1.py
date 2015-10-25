#  https://lorenzod8n.wordpress.com/2007/12/09/pygame-tutorial-4-more-on-events/

import math
import pygame

screen = pygame.display.set_mode((640, 400))
ccolor = (134,0,200)


running = 1

while running:  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = 0
    else:
      print event.type  