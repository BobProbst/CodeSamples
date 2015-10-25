#  https://lorenzod8n.wordpress.com/2007/05/27/pygame-tutorial-2-drawing-lines/

import math
import pygame

hieght = input('Set hieght: ')
width = input('Set width: ')
 
screen = pygame.display.set_mode((width, hieght))

y = 0
x = 0
dir = 1
xdir = 1
running = 1
barheight = 124

barcolor = []
for i in range(1, 63):
  barcolor.append((0, 0, i*4))
for i in range(1, 63):
  barcolor.append((0, 0, 255 - i*4))

while running:  
  event = pygame.event.poll()
  
  if event.type == pygame.QUIT:
    running = 0    
            
  screen.fill([0,0,0])
  
  for i in range(0, barheight):
    pygame.draw.aaline(screen, barcolor[i], (0, y+i), (width-1, y+i))

  y += dir
  if y + barheight > hieght-1 or y < 0:
    dir *= -1   
  
  pygame.display.flip()