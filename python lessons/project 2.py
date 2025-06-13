import math
import random
import pygame
pygame.init()
screen=pygame.display.set_mode((800,500))
bg=pygame.image.load("Photos.jpg")
pygame.display.set_caption("Space Invader Game")
icon=pygame.image.load("Player 1.png")
pygame.display.set_icon(icon)
playerimg=pygame.image.load("Player.png")
playerx=370
playery=380
player_x_change=0
enemy_img=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
enemy_num=6
for i in range(enemy_num):
  enemy_img.append(pygame.image.load("enemy.png"))
  enemy_x.append(random.randint(0,736))
  enemy_y.append(random.randint(50,150))
  enemy_x_change.append(4)
  enemy_y_change.append(40)
bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=380
bulletxchange=0
bulletychange=10
bulletstate="ready"
score=0
font=pygame.font.Font("freesansbold.ttf",32)
text=10
texty=10
gameovertxt=pygame.font.Font("freesansbold.ttf",64)
def show_score(x,y):
  score1=font.render("Score: "+str(score),True,(255,255,255))
  screen.blit(score1,(x,y))
def gameover():
  over_text=font.render("Game Over",True,(255,255,255))
  screen.blit(over_text,(200,250))
def player(x,y):
  screen.blit(playerimg,(x,y))
def enemy(x,y,i):
  screen.blit(enemy_img[i],(x,y))
def firebullets(x,y):
  global bulletstate 
  bulletstate="fire"
  screen.blit(bulletimg,(x+16,y+10))
def iscollision(enemy_x,enemy_y,bulletx,bullety):
  distance=math.sqrt(math.pow(enemy_x-bulletx,2)+math.pow(enemy_y-bullety,2))
  if  distance<27:
    return True
  else:
    return False
running=True
while running:
  screen.fill((0,0,0))
  screen.blit(bg,(0,0))
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      running=False
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_LEFT:
        player_x_change=-5
      if event.key==pygame.K_RIGHT:
        player_x_change=5
      if event.key==pygame.K_SPACE:
        if bulletstate=="ready":
          bulletx=playerx
          firebullets(bulletx,bullety)
    if event.type==pygame.KEYUP:
      if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
        player_x_change=0
  playerx +=player_x_change
  if playerx<=0:
    playerx=0
  elif playerx>=736:
    playerx=736
  for i in range(enemy_num):
    if enemy_y[i]>340: 
      for j in range(enemy_num):
        enemy_y[j]=2000
      gameover()
      break
    enemy_x[i] += enemy_x_change[i]
    if enemy_x[i] <= 0:
            enemy_x_change[i] = 4
            enemy_y[i] += enemy_y_change[i]
    elif enemy_x[i] >= 736:
      enemy_x_change[i] = -4
      enemy_y[i] += enemy_y_change[i]
    collision = iscollision(enemy_x[i], enemy_y[i], bulletx, bullety)
    if collision:
      bullety = 380
      bulletstate = "ready"
      score += 1
      enemy_x[i] = random.randint(0, 736)
      enemy_y[i] = random.randint(50, 150)
    enemy(enemy_x[i], enemy_y[i], i)
  if bullety <= 0:
    bullety = 380
    bulletstate = "ready"
  if bulletstate == "fire":
    firebullets(bulletx, bullety)
    bullety -= bulletychange
  player(playerx, playery)
  show_score(text,texty)
  pygame.display.update()
