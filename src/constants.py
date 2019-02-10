from random import randint

floor_number = randint(1, 2)
level_number = randint(1, 2)
wall_number = randint(1, 2)


#############
# Images path
#############
BACKGROUNG_IMG = 'images/background_img.png'
ENEMY_IMG = 'images/Gardien.png'
ETHER_IMG = 'images/ether.png'
FLOOR_IMG = f'images/floor_{floor_number}.png'
HERO_IMG = 'images/MacGyver.png'
PLASTIC_TUBE_IMG = 'images/tube_plastique.png'
NEEDLE_IMG = 'images/aiguille.png'
WALL_IMG = f'images/wall_{wall_number}.png'

#############
# Level
#############
FILE_LEVEL = f'levels/level_{level_number}.txt'

############
# Others
############
NB_SPRITE = 15
SPRITE_SIZE = 30

#############
# Windows parameters
#############
WINDOW_SIZE = (SPRITE_SIZE * NB_SPRITE, SPRITE_SIZE * NB_SPRITE)
