# Python Project

# Title : Project Ball Game
# Date : 2020-07-09
# Creator : tunealog

import os
import pygame
##################################################################
# Basic Initialize
pygame.init()

# Screen Size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title
pygame.display.set_caption("Tune a Pang")

# FPS
clock = pygame.time.Clock()
##################################################################

# 1. User Initialize
# Create File Path
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# Create Background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Create Stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# Create Character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height


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
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # Update Display
    pygame.display.update()

# pygame Quit
pygame.quit()
