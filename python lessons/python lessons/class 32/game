import pygame
pygame.init()

Height = 600
Width = 600

screen = pygame.display.set_mode((Height, Width))
runningstate = True

import random

batX = 250
batY = 450

ballX = random.randint(0, 550)

ballY = 30

colorList = ["red", "green", "pink", "yellow", "purple", "orange", "black", "grey",]


class Bat(pygame.sprite.Sprite):

  def __init__(self):
   super().__init__()
   self.image = pygame.Surface((150, 50))
   self.image.fill("blue")
   self.rect = self.image.get_rect()

   self.rect.x = batX
   self.rect.y = batY

class Ball(pygame.sprite.Sprite):

    def __init__(self):
      super().__init__()

      self.image = pygame.Surface((50, 50),pygame.SRCALPHA)

      pygame.draw.circle(self.image, random.choice(colorList), (20,20), 20)

      self.rect = self.image.get_rect()
      self.rect.x =random.randint(0, 550)
      self.rect.y = ballY

def update(self):

     self.rect.y += 1

bat = Bat()
ball = Ball()

enemy = pygame.sprite.Group()
enemy.add(ball)

clock = pygame.time.Clock()

player = pygame.sprite.Group()
player.add(bat)

count = 0

while runningstate:
     screen.fill("white")

player.draw(screen)
count += 1

if count == 100:
    print(count)

ball = Ball()

enemy.add(ball)
count = 0
enemy.draw(screen)
enemy.update()

for event in pygame.event.get():

    if event.type == pygame.QUIT:
      runningstate = False

if event.type == pygame.KEYDOWN:
  if event.key == pygame.K_RIGHT and batX < Width - 150:

   bat.rect.x += 10

if event.key == pygame.K_LEFT and batX > 0:
   bat.rect.x -= 10

if pygame.sprite.spritecollide(bat, enemy, True):

    pygame.display.update()

clock.tick(60)