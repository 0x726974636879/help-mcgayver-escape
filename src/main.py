import pygame
from constants import (
    BACKGROUNG_IMG,
    FILE_LEVEL,
    HERO_IMG,
    WINDOW_SIZE
)
from utils.models import *

# Initialize pygame
pygame.init()

# Create the window
window = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)

background_image = pygame.image.load(ENEMY_IMG).convert_alpha()

# Condition loop for the menu
menu = True
# Condition loop for the game continue
play = False
while menu:
    # Catch user events
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and
                event.key == pygame.K_ESCAPE):
            menu = False
        elif event.type == pygame.K_F1:
            # Initialize the level.
            level = Level(FILE_LEVEL)
            level.generate_level()
            level.init_items()
            level.get_initial_positions()
            player_start_position = level.positions['player']
            end_position = level.positions['end']
            items_position = level.positions['items']
            walls_position = level.positions['walls']

            # Initialize the characters.
            player = Player(HERO_IMG, player_start_position,
                            end_position, items_position, walls_position)
            menu = False
            play = True
        window.blit(BACKGROUNG_IMG, (0, 0))
        pygame.display.flip()

    while play:
        # Catch user events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                    event.type == pygame.KEYDOWN and
                    event.key == pygame.K_ESCAPE):
                play = False
                menu = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_RIGHT or
                        event.key == pygame.K_DOWN or
                        event.key == pygame.K_LEFT):
                    # Change the position of the main character.
                    player.move_player(event.key)
                    # Check if we have some item to remove in the structure
                    if player.item_collected is not None:
                        item_position = player.item_collected
                        level.remove_item(item_position)
                        player.item_collected = None
        # Show the level.
        level.show_level(window)
        # Show the character.
        player.show_player(window)
        # Re-initialize the display.
        pygame.display.flip()
        # Check if the player has all the items to stop the game.
        if player.is_finish is True:
            play = False

pygame.quit()
