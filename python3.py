#  https://lorenzod8n.wordpress.com/2007/05/30/pygame-tutorial-3-mouse-events/

import math
import pygame

screen = pygame.display.set_mode((640, 400))
ccolor = (134,0,200)

x = y = 0
running = 1
pygame.mouse.set_visible(False)

while running:  
  event = pygame.event.poll()
 
  if event.type == pygame.QUIT:
    running = 0
  elif event.type == pygame.MOUSEMOTION:
    x, y = event.pos

  screen.fill([0,0,0])      
  pygame.draw.circle(screen,ccolor,[x,y],20)
  pygame.draw.line(screen,ccolor,(x,0),(x,399))      
  pygame.draw.line(screen,ccolor,(0,y),(639,y))      
  
  pygame.display.flip()