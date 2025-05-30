import random
import pygame

def new_func():
    pygame.init()

    Height = 600
    Width = 600

    screen = pygame.display.set_mode((Height,Width))

    circle_x = 0
    circle_Y = 100

    runing_state = True

    while runing_state:
        screen.fill((139,21,194))
        pygame.draw.circle(screen,"Green",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"pink",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"White",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Yellow",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"purple",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Blue",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Violet",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"red",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"orange",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Black",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"indigo",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),0)
        pygame.draw.circle(screen,"grey",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Magenta",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Brown",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Cyan",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Gold",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"silver",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Navy",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"Coral",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"dark green",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        pygame.draw.circle(screen,"dark blue",(circle_x+random.randint(1,100),circle_Y+random.randint(0,100)),20)
        
        circle_x += 1
        if circle_x > Width:
           circle_x = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("The button x have been clicked")
                runing_state = False

        pygame.display.flip()
    
    pygame.quit

new_func()
