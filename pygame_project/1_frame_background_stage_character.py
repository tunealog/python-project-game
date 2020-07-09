# Python Project

# Title : Project Ball Game
# Date : 2020-07-09
# Creator : tunealog


import pygame
##################################################################
# Basic Initialize
pygame.init()

# Screen Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title
pygame.display.set_caption("Tune a Game")

# FPS
clock = pygame.time.Clock()
##################################################################

# 1. User Initialize

# Event Loop
running = True
while running:

    # FPS Setup
    dt = clock.tick(60)

    # 2. Event Process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Locate Character

    # 4. Collision Process

    # 5. Display to Screen

    # Update Display
    pygame.display.update()

# pygame Quit
pygame.quit()
