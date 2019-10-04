import sys, pygame
from pygame.locals import *
pygame.init()

size = width, height = 800, 600
ball_speed = [3, 7]
black = 0, 0, 0
rod_speed = [5,0]
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 16)

ball_img = pygame.image.load("image.jpeg")
ball = pygame.transform.scale(ball_img,(80,50))
ballrect = ball.get_rect()

rod_img = pygame.image.load("rod.png")
rod = pygame.transform.scale(rod_img,(100,20))
rodrect = rod.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #for ball
    ballrect = ballrect.move(ball_speed)
    if ballrect.left < 0 or ballrect.right > width:
        ball_speed[0] = -ball_speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        ball_speed[1] = -ball_speed[1]
    #for rod
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

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(rod, rodrect)
    screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
    pygame.display.flip()
