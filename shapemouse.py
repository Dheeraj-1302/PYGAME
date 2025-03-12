import pygame

pygame.init()



radius=60
color=[20,40,60]
coordinates = []
def circle(a,b,c):
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    un_loop = True
    while un_loop:
        screen.fill([105,60,200])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                un_loop = False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos_tion =event.pos
                coordinates.append(pos_tion)
        for x in coordinates:
            pygame.draw.circle(screen,color,x,radius)

        pygame.display.update()

pygame.quit()

circle(radius,color,coordinates)


"hello"