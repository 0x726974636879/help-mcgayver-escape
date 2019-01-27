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
positions = level.get_initial_positions()


# Initialize the characters.
main_character = Character(HERO_IMG)
main_character_position = positions['start']
enemy = Character(ENEMY_IMG)
enemy_position = positions['end']

# Condition loop for the game continue
play = True
while play:
    # Catch user events
    for event in pygame.event.get():
        # Catch if the user want to quit the game.
        if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key == pygame.K_ESCAPE):
            play = False
        # Catch if the user press another key.
        if event.type == pygame.KEYDOWN:
            # Change the position of the main character.
            main_character_position = main_character.move_character(
                event.key, main_character_position)

    # Show the level.
    level.show_level(window)
    # Show the characters.
    main_character.show_character(window, main_character_position)
    enemy.show_character(window, enemy_position)

    # Re-initialize the display.
    pygame.display.flip()


pygame.quit()
