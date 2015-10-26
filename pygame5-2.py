#  https://lorenzod8n.wordpress.com/2007/12/16/pygame-tutorial-5-pixels/

import math
import random
import pygame
#import pygame.freetype

width = 600
hieght = 400

WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((width, hieght))
clock = pygame.time.Clock()

running = True

pygame.mouse.set_visible(False)

#######################################################

pygame.font.init()  

#pixel postion
x = width/2 
y = hieght/2

#pixel direction
dir_x = 0
dir_y = -1

screen.fill(BLACK)

def randomColor():
  return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  
def Crash(surf, loc): 
  x,y = loc 
  f = pygame.font.SysFont("freesansbold.ttf",36)
  a,b = f.size("CRASH!")
  cr = f.render("CRASH!",True,(255,0,0))   
  surf.blit(cr,(x-(a/2),y-(b/2)))

while running: 
  x += dir_x
  y += dir_y
  
  c = screen.get_at((x,y))  
  
  if (x <= 0 or
        x >= width - 1 or
        y <= 0 or
        y >= hieght - 1 or 
        (c.r, c.g, c.b) != BLACK):
    Crash(screen, (x,y))
    pygame.display.flip()
    running = False
    pygame.time.wait(3000)
    
  #screen.fill(BLACK) 
  screen.set_at((x,y), WHITE)  
   
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False  
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        dir_x = 0
        dir_y = -1
      elif event.key == pygame.K_DOWN:
        dir_x = 0
        dir_y = 1
      elif event.key == pygame.K_LEFT:
        dir_x = -1
        dir_y = 0      
      elif event.key == pygame.K_RIGHT:
        dir_x = 1
        dir_y = 0      
    

  pygame.display.flip()
  
  clock.tick(140)    