#  https://lorenzod8n.wordpress.com/2007/05/27/pygame-tutorial-2-drawing-lines/

import math
import pygame

size = input('Set size: ')
increment = input('Set line increment: ')
line_count = math.floor(size/increment)
 
screen = pygame.display.set_mode((size, size))

running = 1
blue = (0,0,255)


def drawLines(scr, color, inc, corner):
  """Draw lines around the corner
      scr = pygame.Surface object
      color = RGB (255,255,255)
      inc = how many pixels to increment each line
      corner = which corner to draw out of (1,2,3,4)
  
  """  
  sz = size
  lineCount = math.floor(sz/inc)
  
  for i in range(int(lineCount)+1):
    decreasing = size-(i*inc)-1
    increasing = i*inc 
    
    if corner == 1:
      edge1 = (0,decreasing)
      edge2 = (increasing,0)
    elif corner == 2:
      edge1 = (increasing,0)
      edge2 = (sz-1,increasing)    
    elif corner == 3:
      edge1 = (sz-1,increasing)
      edge2 = (decreasing,sz-1)    
    else:
      edge1 = (0,increasing)
      edge2 = (increasing,sz-1)    
    
    pygame.draw.aaline(scr, color, edge1, edge2)



while running:  
  event = pygame.event.poll()
  if event.type == pygame.QUIT:
    running = 0    
            
  screen.fill((0,0,0))
  
  drawLines(screen,blue,increment,1)
  drawLines(screen,blue,increment,2)
  drawLines(screen,blue,increment,3)
  drawLines(screen,blue,increment,4)
  pygame.display.flip()
