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

# Load Background Image
background = pygame.image.load(
    "/Users/macbookair/Desktop/python/python-project-game/pygame_basic/background.png")

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background Display
    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 255))

    # Update Display
    pygame.display.update()

# pygame Quit
pygame.quit()
