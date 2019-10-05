import sys, pygame
from pygame.locals import *
import time
import pygame.freetype

pygame.init()

size = width, height = 800, 600
ball_speed = [3, 7]
black = 0, 0, 0
rod_speed = [5,0]
score = 1

green = (0, 255, 0)
blue = (0, 0, 128)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

#ball loading and shortning its image size
ball_img = pygame.image.load("image.jpeg")
ball = pygame.transform.scale(ball_img,(80,50))
ballrect = ball.get_rect()

#setting the caption for game
pygame.display.set_caption("Rod and Ball Game")

#rod loading and shortning its image size
rod_img = pygame.image.load("rod.png")
rod = pygame.transform.scale(rod_img,(100,20))
rodrect = rod.get_rect()

font = pygame.font.Font('freesansbold.ttf', 32)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #image collision function added
    if ballrect.colliderect(rodrect):
        score +=1
        #print(score)
    elif ballrect.top < 0:
        print(score)
        screen.fill(white)
        text = font.render('Your Score ' + str(score), True, green, blue)
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 2)
        screen.blit(text, textRect)

        pygame.display.update()

        pygame.quit()
        pygame.time.delay(2000)
        quit()

    #ball code
    ballrect = ballrect.move(ball_speed)
    if ballrect.left < 0 or ballrect.right > width:
        ball_speed[0] = -ball_speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        ball_speed[1] = -ball_speed[1]

    #rod code
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if rod_speed[0] > 0:
                rod_speed[0] = -rod_speed[0]
        elif event.key == pygame.K_LEFT:
            if rod_speed[0] < 0:
                rod_speed[0] = -rod_speed[0]

    rodrect = rodrect.move(rod_speed)

    if rodrect.left < 0 or rodrect.right > width:
        rod_speed[0] = -rod_speed[0]

    #screen pixels and setting adjustment
    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(rod, rodrect)

    #turning full image upside down
    screen.blit(pygame.transform.rotate(screen, 180), (0, 0))


    pygame.display.flip()
