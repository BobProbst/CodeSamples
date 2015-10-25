#  https://lorenzod8n.wordpress.com/2007/05/25/pygame-tutorial-1-getting-started/
 
import pygame
 
screen = pygame.display.set_mode((640, 400))

running = 1

while running:  
    
  for r in range(256):
    for g in range(256):
      for b in range(256):  
      
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
          running = 0    
            
        screen.fill((r,g,b))
        pygame.display.flip()
