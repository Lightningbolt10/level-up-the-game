import pygame
import random
pygame.init()


sw = 500
sh =  400
font = pygame.font.SysFont("Times New Roman",72)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        

    def move(self,xc,yc):
       self.rect.x = max(min(self.rect.x+xc,sw-self.rect.width),0)
       self.rect.y = max(min(self.rect.y+yc,sh-self.rect.height),0)

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(pygame.Color("white") ,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

sp2 = Sprite(pygame.Color("green") ,30,70)
sp2.rect.x = random.randint(0,430)
sp2.rect.y = random.randint(0,370)
all_sprites_list.add(sp2)

screen = pygame. display.set_mode((sw,sh))
pygame. display.set_caption("Boundry sprite")
bg_color = pygame.Color("blue")
screen.fill(bg_color)
won = False
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
         running = False
    if not won:
       keys = pygame.key.get_pressed()
       xc = (keys[pygame.K_RIGHT]- keys[pygame.K_LEFT]) * 5
       yc = (keys[pygame.K_DOWN]- keys[pygame.K_UP]) * 5
       sp1.move(xc,yc)
       
       if sp1.rect.colliderect(sp2.rect):
          all_sprites_list.remove(sp2)
          won = True

    screen.fill(bg_color)

    if won:
       win_text = font.render("You Win!",True, pygame.Color("Black"))
       screen.blit(win_text, ((sw - win_text.get_width()) //2,(sh - win_text.get_height()) //2))

         

    all_sprites_list.update()
    
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()

    
   
          
        
        

        

    

        
    