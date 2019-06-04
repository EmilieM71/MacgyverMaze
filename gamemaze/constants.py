"""Game constants"""

# Constants file
START_CHAR = 's'
END_CHAR = 'e'
PATH_CHAR = '.'
WALL_CHAR = 'w'

# Game setting
NUMBER_SPRITE_COTE = 15
CASE_SIZE = 30
COTE_SCREEN_GAME = NUMBER_SPRITE_COTE * CASE_SIZE
BANNER_SIZE = 210
COTE_WINDOW = COTE_SCREEN_GAME + BANNER_SIZE

# Customizing the Window
TITLE_WINDOW = "Aidez MacGyver à s'échapper !"
IMAGE_ICON = "resource/images/tile-crusader-logo.png"

# GAME IMAGE LIST
FLOOR_TILES = "resource/images/floor-tiles-20x20.png"
STRUCTURE_WALL = "resource/images/structures.png"
HERO_SOURCE = "resource/images/personnages.png"
KEEPER_IMAGE = "resource/images/Gardien.png"
NEEDLE_IMAGE = "resource/images/aiguille.png"
ETHER_IMAGE = "resource/images/ether.png"
TUBE_IMAGE = "resource/images/tube_plastique.png"
SYRINGE_IMAGE = "resource/images/seringue.png"
MACGYVER_SOURCE = "resource/images/MacGyver.png"
BLOOD_STAIN = "resource/images/items.png"

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# HOME TEXT (text, font_size, font_color, background_color,
# position_x, position_y)
HOME_TEXTS = [["Appuie sur ESCAPE pour quitter ou ENTER pour rejouer", 455],
              ["Aide MacGyver à s'échapper du Labyrinthe !", 490],
              ["Récupère l'aiguille, le tube et l'ether, afin de", 520],
              ["fabriquer une seringue. Tu pourras ainsi", 550],
              ["endormir le gardien,et sortir du labyrinthe !", 580]]
