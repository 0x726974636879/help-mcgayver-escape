import pygame
from constants import (
    ENEMY_IMG,
    FILE_LEVEL,
    HERO_IMG,
    WINDOW_SIZE
)
from utils.objects import (
    Character,
    Level
)

# Initialize pygame
pygame.init()

# Create the window
window = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

# Initialize the level.
level = Level(FILE_LEVEL)
characters_position = level.characters_position
walls_position = level.walls_position

# Initialize the characters.
main_character = Character(HERO_IMG, walls_position)
main_character.position = characters_position['start']
enemy = Character(ENEMY_IMG, walls_position)
enemy.position = characters_position['end']

# Condition loop for the game continue
play = True
while play:
    # Catch user events
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key == pygame.K_ESCAPE):
            play = False
        if event.type == pygame.KEYDOWN:
            # Change the position of the main character.
            main_character.move_character(event.key)

    # Show the level.
    level.show_level(window)
    # Show the main character.
    main_character.show_character(window)
    enemy.show_character(window)

    # Re-initialize the display.
    pygame.display.flip()


pygame.quit()
