# Python Project (Ball Game)

# Title : Sprite
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

# Load Sprite
character = pygame.image.load(
    "/Users/macbookair/Desktop/python/python-project-game/pygame_basic/character.png")

# Get Image Size
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

# Position of Image
character_x_pos = (screen_width / 2) - (character_height / 2)
character_y_pos = screen_height - character_height

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background Display
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    # Update Display
    pygame.display.update()

# pygame Quit
pygame.quit()
