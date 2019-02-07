import pygame

from constants import (
    ENEMY_IMG,
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
        self.file = file
        self.level_structure = []
        self.positions = {
            'player': None,
            'end': None,
            'items': {
                'ether': None,
                'needle': None,
                'plastic_tube': None,
                'syringe': None,
            },
            'walls': []
        }
        self.items_image = {}

    def remove_item(self, item_position):
        """
        Remove an item in the structure's level
        to remove the item on the map.

        :param item_position: Item's position that the player
                              has recently taken.
        """
        x = int(item_position[1] / SPRITE_SIZE)
        y = int(item_position[0] / SPRITE_SIZE)
        self.level_structure[x][y] = 'f'

    def generate_level(self):
        """
        Read a level file then return a list with
        the position of all sprites.
        """
        # Open the file.
        with open(self.file, 'r') as f:
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
                self.level_structure.append(row_level)

    def get_initial_positions(self):
        """
        Reading the level_structure list then get
        the initial position of all items on the map.
        """
        for y, row in enumerate(self.level_structure):
            for x, letter in enumerate(row):
                position = (
                    SPRITE_SIZE * x,
                    SPRITE_SIZE * y
                )
                if letter == 's':
                    self.positions['player'] = position
                elif letter == 'e':
                    self.positions['end'] = position
                elif letter == 'w':
                    self.positions['walls'].append(position)
                elif letter == '1':
                    self.positions['items']['ether'] = position
                elif letter == '2':
                    self.positions['items']['needle'] = position
                elif letter == '3':
                    self.positions['items']['plastic_tube'] = position
                elif letter == '4':
                    self.positions['items']['syringe'] = position

    def show_level(self, window):
        """
        Reading the level_structure list then show
        the level in the window game.

        :param window: pygame display object.
        """
        # Run through the level structure list to put
        # each image at the good place.
        for y, row in enumerate(self.level_structure):
            for x, letter in enumerate(row):
                position = (
                    SPRITE_SIZE * x,
                    SPRITE_SIZE * y
                )
                if (letter == 'e' or letter == 'f' or letter == 's' or
                    letter == '1' or letter == '2' or letter == '3' or
                        letter == '4'):
                    window.blit(self.items_image['floor'], position)
                    if letter == 'e':
                        window.blit(self.items_image['enemy'], position)
                    if letter == '1':
                        window.blit(self.items_image['ether'], position)
                    elif letter == '2':
                        window.blit(self.items_image['needle'], position)
                    elif letter == '3':
                        window.blit(
                            self.items_image['plastic_tube'], position)
                    elif letter == '4':
                        window.blit(self.items_image['syringe'], position)
                elif letter == 'w':
                    window.blit(self.items_image['wall'], position)

    def init_items(self):
        """
        Initialiaze all images make them to the good size.
        """
        self.items_image['enemy'] = pygame.transform.scale(
            pygame.image.load(ENEMY_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.items_image['ether'] = pygame.transform.scale(
            pygame.image.load(ETHER_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.items_image['floor'] = pygame.transform.scale(
            pygame.image.load(FLOOR_IMG).convert(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.items_image['needle'] = pygame.transform.scale(
            pygame.image.load(NEEDLE_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.items_image['plastic_tube'] = pygame.transform.scale(
            pygame.image.load(PLASTIC_TUBE_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.items_image['syringe'] = pygame.transform.scale(
            pygame.image.load(SYRINGE_IMG).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        self.items_image['wall'] = pygame.transform.scale(
            pygame.image.load(WALL_IMG).convert(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )


class Player:
    """
    Create a character and allow it to move.
    """

    def __init__(self, image, start, end, items_position, walls):
        self.end_position = end
        self.is_finish = False
        self.image = image
        self.items_position = items_position
        self.items = {
            'ether': False,
            'needle': False,
            'plastic_tube': False,
            'syringe': False,
        }
        self.item_collected = None
        self.position = start
        self.walls_position = walls

    def show_player(self, window):
        """
        Show the character on the map.

        :param window: pygame display object.
        """
        player = pygame.transform.scale(
            pygame.image.load(self.image).convert_alpha(),
            (SPRITE_SIZE, SPRITE_SIZE)
        )
        window.blit(player, self.position)

    def move_player(self, key):
        """
        Move the player on the map.

        :param key: key that the player pressed.
        """
        previous_position = self.position
        # Go to the good direction when the good
        # key has been pressed.
        if key == pygame.K_UP:
            self.position = (
                self.position[0],
                self.position[1] - SPRITE_SIZE
            )
        elif key == pygame.K_RIGHT:
            self.position = (
                self.position[0] + SPRITE_SIZE,
                self.position[1]
            )
        elif key == pygame.K_DOWN:
            self.position = (
                self.position[0],
                self.position[1] + SPRITE_SIZE
            )
        elif key == pygame.K_LEFT:
            self.position = (
                self.position[0] - SPRITE_SIZE,
                self.position[1]
            )
        # Check if the player is going to a wall, a item or
        # to the end position.
        self.check_position(self.position, previous_position)

    def check_position(self, current_position, previous_position):
        """
        Check the player's position to do the good action.

        :param current_position: the current player's position.
        :param previous_position: the previous player's position.
        """
        # If the player has all the items and is on the end position
        # finish the game.
        if (self.position == self.end_position):
            if (self.items['ether'] and self.items['needle'] and
                    self.items['plastic_tube'] and self.items['syringe']):
                self.is_finish = True
        # If the position the player tried to go is a wall
        # or out of the window then the player get back
        # to the previous position.
        elif (self.position in self.walls_position or
              self.position[0] > WINDOW_SIZE[0] - SPRITE_SIZE or
              self.position[0] < 0 or
              self.position[1] > WINDOW_SIZE[1] - SPRITE_SIZE or
                self.position[1] < 0):
            self.position = previous_position
        else:
            # If the player is on a item assignate True to the item.
            for name, position in self.items_position.items():
                if self.position == position:
                    self.item_collected = position
                    self.items[name] = True
