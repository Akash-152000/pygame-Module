import pygame,sys
from pygame.locals import *

pygame.init()
DISPLAYSURF=pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Drawing")

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

DISPLAYSURF.fill(WHITE)

pygame.draw.polygon(DISPLAYSURF,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.line(DISPLAYSURF,BLUE,(220,330),(400,300))
pygame.draw.circle(DISPLAYSURF,RED,(400,300),20,3)
pygame.draw.rect(DISPLAYSURF,GREEN,(200,300,400,150),6)

pixObj=pygame.PixelArray(DISPLAYSURF)
pixObj[480][380]=BLACK
pixObj[481][380]=BLACK
pixObj[482][380]=BLACK
pixObj[483][380]=BLACK
pixObj[484][380]=BLACK
del pixObj

while True:
    for event in pygame.event.get():
        pygame.Color(255,0,0)
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
