"""import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dragon Following Mouse")

# Load the dragon image
dragon_image = pygame.image.load("D:\pngwing.com.png")  # Make sure to have a 'dragon.png' image in the same directory
dragon_rect = dragon_image.get_rect()

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with a white color

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Update the position of the dragon image to follow the mouse cursor
    dragon_rect.center = (mouse_x, mouse_y)

    # Draw the dragon on the screen
    screen.blit(dragon_image, dragon_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
"""


import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display window
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dragon Facing Mouse")

# Load the dragon image (ensure the image is pointing in the default direction, e.g., facing right)
dragon_image = pygame.image.load("D:\pngwing.com.png")  # Replace with your dragon image path
dragon_rect = dragon_image.get_rect()

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with a white background

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the angle between the dragon and the mouse cursor
    dx = mouse_x - dragon_rect.centerx
    dy = mouse_y - dragon_rect.centery
    angle = math.degrees(math.atan2(dy, dx))  # Convert angle from radians to degrees

    # Rotate the dragon image to face the mouse
    rotated_dragon = pygame.transform.rotate(dragon_image, -angle)
    rotated_rect = rotated_dragon.get_rect(center=dragon_rect.center)

    # Draw the rotated dragon image on the screen
    screen.blit(rotated_dragon, rotated_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
