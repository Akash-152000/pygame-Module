import pygame,sys
from pygame.locals import *
import time
import random

pygame.init()
clock=pygame.time.Clock()

surf=pygame.display.set_mode((500,500))
pygame.display.set_caption("Learning")
black=(0,0,0)
white=(255,255,255)
ct=pygame.image.load("racecar.png")



car_speed=0

car_width=73



def messageDisplay(text,font):
    textSurf=font.render(text,True,black)
    return textSurf, textSurf.get_rect()

def crash():
    text="You crashed"
    font=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=messageDisplay(text,font)
    textrect.center=(500/2,500/2)
    surf.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2)
    gameLoop()

def things(thingx,thingy,thingw,thingh):
    pygame.draw.rect(surf,(255,0,0),[thingx,thingy,thingw,thingh])

def gameLoop():
    x=500*0.40
    y=400
    crashed=True
    x_change=0
    
    thing_x=random.randrange(0,500)
    thing_y=-600
    thing_speed=7
    thing_width=100
    thing_height=100

    
    while crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               crashed=False


            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and x>=100:
                    x_change=-5
                if event.key==pygame.K_RIGHT and x<470:
                    x_change=5

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
    
        x+=x_change
        surf.fill(white)

        things(thing_x,thing_y,thing_width,thing_height)
        thing_y+=thing_speed
        surf.blit(ct,(x,y))
        
        if x>500-car_width or x<0:
            crash()
        
        if thing_y>500:
            thing_y=0-thing_height
            thing_x=random.randrange(0,400)

        if y < thing_y+thing_height:
            print('y crossover')

            if x > thing_x and x < thing_x + thing_width or x+car_width > thing_x and x + car_width < thing_x+thing_width:
                print('x crossover')
                crash()
        
        
        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
sys.exit()
