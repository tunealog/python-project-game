# Python Project (Ball Game)

# Title : Keyboard Event
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

# Move Position
to_x = 0
to_y = 0

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # Background Display
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    # Update Display
    pygame.display.update()

# pygame Quit
pygame.quit()
