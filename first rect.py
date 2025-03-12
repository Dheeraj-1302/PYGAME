# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))
color="green"
# Fill the scree with white color
#window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the outlined rectangle
#pygame.draw.rect(window, (0, 0, 255),
	#			[100, 100, 400, 100], 2)

# Draws the surface object to the screen.
pygame.display.update()
Unloop = True
while Unloop:
    window.fill("white")
    # Creating a list of different rects
    rectangle_list = [pygame.Rect(50, 100, 500, 200),
                      pygame.Rect(70, 120, 460, 160),
                      pygame.Rect(90, 140, 420, 120),
                      pygame.Rect(110, 160, 380, 80),
                      pygame.Rect(130, 180, 340, 40)
                      ]
    # Creating list of different colors
    color_list = [(0, 0, 0),
                  (255, 255, 255),
                  (0, 0, 255),
                  (0, 255, 0),
                  (255, 0, 0)
                  ]
    color_Var=0
    for rectangle in rectangle_list:
        pygame.draw.rect(window,color_list[color_Var],
                         rectangle)
        color_Var+=1
#    pygame.draw.circle(window,"red",(300,300),135)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Unloop=False
    pygame.display.update()
pygame.quit()