#  https://lorenzod8n.wordpress.com/2007/05/30/pygame-tutorial-3-mouse-events/

import math
import pygame

screen = pygame.display.set_mode((640, 400))
ccolor = (134,0,200)

UP = 1
DOWN = 2

x = y = 0
LEFT = 1
running = 1
#pygame.mouse.set_visible(False)
btnState = UP 



while running:  
  event = pygame.event.poll()
 
  if event.type == pygame.QUIT:
    running = 0
  elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
    x, y = event.pos
    btnState = DOWN
  elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
    btnState = UP
  elif event.type == pygame.MOUSEMOTION:
    x, y = event.pos  

  screen.fill([0,0,0])      
  #pygame.draw.circle(screen,ccolor,[x,y],20)
  if btnState == DOWN:
    pygame.draw.line(screen,ccolor,(x-20,y),(x+20,y))      
    pygame.draw.line(screen,ccolor,(x,y-20),(x,y+20))      
  
  pygame.display.flip()