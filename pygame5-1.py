#  https://lorenzod8n.wordpress.com/2007/12/16/pygame-tutorial-5-pixels/

import math
import pygame
import random

width = 600
hieght = 400

x = y = 0
screen = pygame.display.set_mode((width, hieght))
ccolor = (0,0,0)
clock = pygame.time.Clock()

running = True
pygame.mouse.set_visible(False)

def randomColor():
  return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

while running:  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False  
    
  x = random.randint(0, width-1)
  y = random.randint(0, hieght-1)  
  screen.set_at((x,y), randomColor())      

  pygame.display.flip()
  
  clock.tick(240)    