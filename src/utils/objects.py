import pygame

from constants import (
    ETHER_IMG,
    FLOOR_IMG,
    NEEDLE_IMG,
    PLASTIC_TUBE_IMG,
    SPRITE_SIZE,
    SYRINGE_IMG,
    WALL_IMG,
    WINDOW_SIZE
)


class Level:
    """
    Create a level, on analyze the file structure
    of the level.
    """

    def __init__(self, file):
        self.level_structure = self.generate_level(file)
        self.characters_position = None
        self.objects_image = {}
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
        # Run through the level structure list to put
        # each image at the good place.
        self.init_objects()
        for y, row in enumerate(self.level_structure):
            for x, letter in enumerate(row):
                position = (
                    SPRITE_SIZE * x,
                    SPRITE_SIZE * y
                )
                if (letter == 'e' or letter == 'f' or letter == 's' or
                    letter == '1' or letter == '2' or letter == '3' or
                        letter == '4'):
                    window.blit(self.objects_image['floor'], position)
                    if letter == '1':
                        window.blit(self.objects_image['ether'], position)
                    elif letter == '2':
                        window.blit(self.objects_image['needle'], position)
                    elif letter == '3':
                        window.blit(
                            self.objects_image['plastic_tube'], position)
                    elif letter == '4':
                        window.blit(self.objects_image['syringe'], position)
                elif letter == 'w':
                    window.blit(self.objects_image['wall'], position)

    def init_objects(self):
        """
        Initialiaze all images make them to the good size.
        """
        self.objects_image['ether'] = pygame.transform.scale(
            pygame.image.load(ETHER_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.objects_image['floor'] = pygame.transform.scale(
            pygame.image.load(FLOOR_IMG).convert(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.objects_image['needle'] = pygame.transform.scale(
            pygame.image.load(NEEDLE_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.objects_image['plastic_tube'] = pygame.transform.scale(
            pygame.image.load(PLASTIC_TUBE_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.objects_image['syringe'] = pygame.transform.scale(
            pygame.image.load(SYRINGE_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.objects_image['wall'] = pygame.transform.scale(
            pygame.image.load(WALL_IMG).convert(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )


class Character:
    """
    Create a character and allow it to move.
    """

    def __init__(self, image, walls):
        self.image = image
        self.position = None
        self.walls_position = walls

    def show_character(self, window):
        """
        Show the character on the map.

        :param window: pygame display object.
        """
        image = self.image
        character = pygame.transform.scale(
            pygame.image.load(image).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        window.blit(character, self.position)

    def move_character(self, key):
        """
        Move the caracter on the map.

        :param key: key that the player pressed.
        """
        previous_position = self.position
        x = None
        y = None
        # Go to the good direction when the good
        # key has been pressed.
        if key == pygame.K_UP:
            self.position = (
                previous_position[0],
                previous_position[1] - SPRITE_SIZE
            )
        elif key == pygame.K_RIGHT:
            self.position = (
                previous_position[0] + SPRITE_SIZE,
                previous_position[1]
            )
        elif key == pygame.K_DOWN:
            self.position = (
                previous_position[0],
                previous_position[1] + SPRITE_SIZE
            )
        elif key == pygame.K_LEFT:
            self.position = (
                previous_position[0] - SPRITE_SIZE,
                previous_position[1]
            )

        x = self.position[0]
        y = self.position[1]
        # If the position the player tried to go is a wall
        # or out of the window then the player get back
        # to the previous position.
        if (self.position in self.walls_position or
            x > WINDOW_SIZE[0] - SPRITE_SIZE or x < 0 or
                y > WINDOW_SIZE[1] - SPRITE_SIZE or y < 0):
            self.position = previous_position
