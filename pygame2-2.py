#  https://lorenzod8n.wordpress.com/2007/05/27/pygame-tutorial-2-drawing-lines/

import math
import pygame

hieght = input('Set hieght: ')
width = input('Set width: ')
 
screen = pygame.display.set_mode((width, hieght))

y = 0
x = 0
ydir = 1
xdir = 1
running = 1
linecolor = (0,0,255)
bgcolor = (0,0,0)

while running:  
  event = pygame.event.poll()
  
  if event.type == pygame.QUIT:
    running = 0    
            
  screen.fill(bgcolor)
  
  pygame.draw.aaline(screen,linecolor,(0,y),(width-1,y))
  pygame.draw.aaline(screen,linecolor,(x,0),(x,hieght-1))
  pygame.draw.circle(screen,linecolor,(width-x,hieght-y),20)
  
  y += ydir
  if y == 0 or y == hieght-1:
    ydir *= -1
    
  x += xdir
  if x == 0 or x == width-1:
    xdir *= -1    
  
  pygame.display.flip()
