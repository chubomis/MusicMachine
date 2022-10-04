import pygame, sys

screen_w = 800
screen_h = 800
meh = 148, 233, 100
screen = pygame.display.set_mode((screen_w, screen_h))
red = 255,0,0
circleX = 100
circleY = 100
radius = 300


def change():
    if play == False:
        timer = 0
    if play == True:
        timer =+ tempo


while True:
    play = True
    timer = 0
    tempo = 10
#for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#click x to quit program
            pygame.quit()
            sys.exit()

    if play == False:
        timer = 0
    if play == True:
        timer =+ tempo
    print(timer)
    screen.fill(meh)
    pygame.draw.circle(screen,red,(circleX,circleY),radius)
    pygame.display.flip()

pygame.quit()
quit()
