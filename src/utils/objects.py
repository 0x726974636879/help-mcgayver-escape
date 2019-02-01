import pygame

from constants import (
    FLOOR_IMG,
    SPRITE_SIZE,
    WALL_IMG
)


class Level:
    """
    Create a level, on analyze the file structure
    of the level.
    """

    def __init__(self, file):
        self.level_structure = self.generate_level(file)
        self.characters_position = None
        self.walls_position = None
        self.get_initial_positions()

    def generate_level(self, file):
        """
        Read a level file then return a list with
        the position of all sprites.

        :param file: .txt file modeling the structure of the level.
        :return list of positions of all object.
        """
        # Open the file.
        with open(file, 'r') as f:
            # The list of all row level.
            level = []
            for row in f:
                # List of a row.
                row_level = []
                counter = 0
                while (row[counter] != '\n'):
                    # Catch the letter.
                    letter = row[counter]
                    # Add the letter to the row_level.
                    row_level.append(letter)
                    counter += 1
                # Add the whole row to the level list.
                level.append(row_level)

        return level

    def get_initial_positions(self):
        """
        Reading the level_structure list then get
        the initial position of all characters and walls.
        """
        level_structure = self.level_structure
        characters_position = {
            'start': None,
            'end': None
        }
        walls_position = []

        for y, row in enumerate(level_structure):
            for x, letter in enumerate(row):
                position = (
                    SPRITE_SIZE * x,
                    SPRITE_SIZE * y
                )
                if letter == 's':
                    characters_position['start'] = position
                elif letter == 'e':
                    characters_position['end'] = position
                elif letter == 'w':
                    walls_position.append(position)

        # Set the characters position
        self.characters_position = characters_position

        # Set the walls position
        self.walls_position = walls_position

    def show_level(self, window):
        """
        Reading the level_structure list then show
        the level in the window game.

        :param window: pygame display object.
        """
        # Initialiaze all images make them to the good size.
        floor = pygame.transform.scale(
            pygame.image.load(FLOOR_IMG).convert(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        wall = pygame.transform.scale(
            pygame.image.load(WALL_IMG).convert(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        level_structure = self.level_structure

        # Run through the level structure list to put
        # each image at the good place.
        for y, row in enumerate(level_structure):
            for x, letter in enumerate(row):
                position = (
                    SPRITE_SIZE * x,
                    SPRITE_SIZE * y
                )
                if letter == 'e' or letter == 'f' or letter == 's':
                    window.blit(floor, position)
                elif letter == 'w':
                    window.blit(wall, position)


class Character:
    """
    Create a character and allow it to move.
    """

    def __init__(self, image):
        self.image = image
        self.position = []

    def show_character(self, window, position):
        """
        Show the character on the map.

        :param window: pygame display object.
        :param position: character's position.
        """
        image = self.image
        position = tuple(position)
        character = pygame.transform.scale(
            pygame.image.load(image).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        window.blit(character, position)

    def move_character(self, key, position):
        """
        Move the caracter on the map.

        :param key: key that the player pressed.
        :param position: character's current position.
        :return position: character's next position.
        """
        if key == pygame.K_UP:
            position = (
                position[0],
                position[1] - SPRITE_SIZE
            )
        elif key == pygame.K_RIGHT:
            position = (
                position[0] + SPRITE_SIZE,
                position[1]
            )
        elif key == pygame.K_DOWN:
            position = (
                position[0],
                position[1] + SPRITE_SIZE
            )
        elif key == pygame.K_LEFT:
            position = (
                position[0] - SPRITE_SIZE,
                position[1]
            )
        return position
