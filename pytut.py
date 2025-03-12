import pygame
import sys
pygame.init()

color="purple"
rect="blue"
Icon=pygame.image.load("skull.png")

screen=pygame.display.set_mode((800,600),pygame.RESIZABLE)
pygame.display.set_caption("FIRST GAME")
pygame.display.set_icon(Icon)
pygame.time.wait(1000)


Unloop = True
while Unloop:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Unloop=False
    a=pygame.draw.rect(screen,rect,pygame.Rect(165,200,200,300))
    #pygame.draw.circle(screen,rect,(400,300),75)
    pygame.display.update()
    pygame.display.flip()

    if(rect=="blue"):
        rect="green"

    else:
        rect="blue"


pygame.quit()

