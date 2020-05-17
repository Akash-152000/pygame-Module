import pygame
import random
import os
pygame.init()

        
surface=pygame.display.set_mode((900,600))
pygame.display.set_caption("Template")
pygame.mixer.init()

player_img=pygame.image.load(r"C:\Users\akash\Desktop\PROJECT\Game\Extra animations and enemies\Alien sprites\alienGreen_walk1.png").convert()
   
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
WIDTH=900
HEIGHT=600

fps= 30
clock=pygame.time.Clock()

all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)

gameLoop=True



        
while gameLoop:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameLoop=False

    all_sprites.update()
    surface.fill(blue)
    all_sprites.draw(surface)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
