# Python Project (Ball Game)

# Title : Text
# Date : 2020-07-07
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

# FPS
clock = pygame.time.Clock()

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

# Move Speed
character_speed = 0.6


# Enemy Character
# Load Enemy
enemy = pygame.image.load(
    "/Users/macbookair/Desktop/python/python-project-game/pygame_basic/enemy.png")

# Get Image Size
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

# Position of Image
enemy_x_pos = (screen_width / 2) - (enemy_height / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# Font
game_font = pygame.font.Font(None, 40)

# Total Time
total_time = 10

# Start Time
start_tick = pygame.time.get_ticks()


# Event Loop
running = True
while running:

    # FPS Setup
    dt = clock.tick(60)
    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # rect information update for Collision Process
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Collision Check
    if character_rect.colliderect(enemy_rect):
        print("Collision")
        running = False

    # Background Display
    screen.blit(background, (0, 0))
    # Character Display
    screen.blit(character, (character_x_pos, character_y_pos))
    # Enemy Display
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # Timer Setup
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # Time Over
    if total_time - elapsed_time <= 0:
        print("Time Out")
        running = False

    # Update Display
    pygame.display.update()

# Quit Delay
pygame.time.delay(2000)

# pygame Quit
pygame.quit()
