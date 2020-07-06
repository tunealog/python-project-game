# Python Project (Ball Game)

# Title : Frame
# Date : 2020-07-06
# Creator : tunealog


import pygame

# Initialize
pygame.init()

# Screen Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title
pygame.display.set_caption("Tune a Game")

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame Quit
pygame.quit()
