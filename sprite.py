import pygame
import random
pygame.init()

        
surface=pygame.display.set_mode((900,600))
pygame.display.set_caption("Template")
pygame.mixer.init()
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(green)
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
    surface.fill(black)
    all_sprites.draw(surface)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
