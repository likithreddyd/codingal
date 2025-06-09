import pygame

pygame.init()

Height = 600

Width = 600

screen = pygame.display.set_mode((Height, Width))

runningstate = True

batX = 250

batY = 450

ballX = 200

ballY = 30


class Bat(pygame.sprite.Sprite):
   def __init__(self):
     super().__init__()

     self.image = pygame.Surface((150, 50))
     self.image.fill("blue")
     self.rect = self.image.get_rect()
     self.rect.x = batX
     self.rect.y = batY

bat = Bat()

player = pygame.sprite.Group()
player.add(bat)

while runningstate:

    screen.fill("white")

ballY +=1
player.draw(screen)


for event in pygame.event.get():
    if event.type == pygame.QUIT:

      runningstate = False

    if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_RIGHT and batX < Width - 150:
       bat.rect.x += 10

     if event.key == pygame.K_LEFT and batX > 0:
       bat.rect.x -= 10

pygame.display.update()