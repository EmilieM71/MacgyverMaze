import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from gamemaze.constants import (COTE_WINDOW, IMAGE_ICON, TITLE_WINDOW,
                                HERO_SOURCE, KEEPER_IMAGE, SIZE_SPRITE)
from gamemaze.models.game_image import GameImage
from gamemaze.models.character import Character
from gamemaze.models.hero import Hero
from gamemaze.models.maze import Maze


pygame.init()

# Loading resources :

# 1- Creating the Window with icon and title
window = pygame.display.set_mode((COTE_WINDOW, COTE_WINDOW))
pygame.display.set_icon(pygame.image.load(IMAGE_ICON))
pygame.display.set_caption(TITLE_WINDOW)

# 2- Load image for game
hero = GameImage(HERO_SOURCE, 0, 0, 32, 32, SIZE_SPRITE, SIZE_SPRITE)
keeper = GameImage(KEEPER_IMAGE, 0, 0, 32, 36, SIZE_SPRITE, SIZE_SPRITE)

# 3- Create and load maze
level = Maze('level/level1')
level.load_from_file()

# Variable that continues the loop if = True, stops if = False
main_loop = True

# Main loop
while main_loop:

    # Loop Speed Limitation
    pygame.time.Clock().tick(30)

    # Display maze in window
    level.display(window)

    # Create and display character
    for element in level.Elements:
        if element.Name == 'start':
            position_hero = (element.Position.x, element.Position.y)
            mg = Hero('MacGyver', hero.surface, position_hero)
            mg.display(window)
        elif element.Name == 'end':
            position_guardian = (element.Position.x, element.Position.y)
            guardian = Character('keeper', keeper.surface, position_guardian)
            guardian.display(window)

    for event in pygame.event.get():  # We track the list of all the events received
        # If user quit the program stop or if the user presses a ESCAPE key
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            main_loop = False

    # Refresh the display
    pygame.display.flip()

