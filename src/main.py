import pygame
from constants import (
    FILE_LEVEL,
    HERO_IMG,
    WINDOW_SIZE
)
from utils.models import (
    Character,
    Level
)

# Initialize pygame
pygame.init()

# Create the window
window = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

# Initialize the level.
level = Level(FILE_LEVEL)
level.generate_level()
level.init_items()
level.get_initial_positions()
characters_position = level.positions['character']
end_position = level.positions['end']
items_position = level.positions['items']
walls_position = level.positions['walls']

# Initialize the characters.
main_character = Character(HERO_IMG, characters_position,
                           end_position, items_position, walls_position)

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
            if (event.key == pygame.K_UP or event.key == pygame.K_RIGHT or
                    event.key == pygame.K_DOWN or event.key == pygame.K_LEFT):
                # Change the position of the main character.
                main_character.move_character(event.key)

    # Show the level.
    level.show_level(window)
    # Show the character.
    main_character.show_character(window)

    # Re-initialize the display.
    pygame.display.flip()

    # Check if the player has all the items to stop the game.
    if main_character.is_finish is True:
        play = False


pygame.quit()
