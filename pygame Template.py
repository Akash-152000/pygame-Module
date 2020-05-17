import pygame
import random
pygame.init()

        
surface=pygame.display.set_mode((900,600))
pygame.display.set_caption("Template")
pygame.mixer.init()


black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
WIDTH=900
HEIGHT=600

fps= 30
clock=pygame.time.Clock()


gameLoop=True



        
while gameLoop:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameLoop=False

    surface.fill(black)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
