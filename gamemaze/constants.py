"""Game constants"""

# Constants file
START_CHAR = 's'
END_CHAR = 'e'
PATH_CHAR = '.'
WALL_CHAR = 'w'

# Game setting
NUMBER_SPRITE_COTE = 15
SIZE_SPRITE = 30
COTE_SCREEN_GAME = NUMBER_SPRITE_COTE * SIZE_SPRITE
BANNER_SIZE = 150
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
HOME_SOURCE = "resource/images/MacGyver.png"

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (225, 225, 225)

# HOME TEXT
HOME_TEXTS = [("Press ESCAPE to quit or key F1 to F10 to choose your character", 455),
              ("Aide MacGyver à s'échapper du Labyrinthe !", 490),
              ("Récupère l'aiguille, le tube et l'ether, afin de", 520),
              ("fabriquer une seringue. Tu pourras ainsi", 550),
              ("endormir le gardien,et sortir du labyrinthe !", 580)]
