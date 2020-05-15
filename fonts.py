import pygame,sys
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((400,300))
pygame.display.set_caption("FONT")

WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(0,0,255)
catx=10
caty=10
direction="right"
fontObj=pygame.font.Font("freesansbold.ttf",32)
textSurfaceObj=fontObj.render("Hello world!!",True,GREEN,BLUE)
textRectObj=textSurfaceObj.get_rect()
#textRectObj.center=(200,150)

while True:
    DISPLAYSURF.fill(WHITE)
    if direction=="right":
        catx+=5
        if catx==150:
            direction="down"
    elif direction=="down":
        caty+=5
        if caty==220:
            direction="left"
    elif direction=="left":
        catx-=5
        if catx==10:
            direction="up"
    elif direction=="up":
        caty-=5
        if caty==10:
            direction="right"
    DISPLAYSURF.blit(textSurfaceObj,(catx,caty))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
