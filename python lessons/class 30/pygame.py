import pygame

pygame.init()

Height = 600
Width = 600

screen = pygame.display.set_mode((Height,Width))

runningstate = True

x = 275
y = 540

while runningstate:
    screen.fill("Red")

    pygame.draw.rect(screen,"Green",(x,y,150,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningstate = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x <  Width - 150:
                x += 10
            if event.key == pygame.K_RIGHT and x >  0:
                x -= 10

            pygame.display.update()
