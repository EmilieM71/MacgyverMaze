import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT, K_DOWN, K_UP
from gamemaze.constants import (COTE_WINDOW, IMAGE_ICON, TITLE_WINDOW, GRAY,
                                COTE_SCREEN_GAME, BANNER_SIZE, WHITE,
                                HERO_SOURCE, BLACK, SIZE_SPRITE)
from gamemaze.models.game_image import GameImage
from gamemaze.models.game_window import GameWindow
from gamemaze.models.hero import Hero
from gamemaze.models.game_maze import GameMaze


pygame.init()

# Loading resources :
window = GameWindow(COTE_WINDOW, COTE_WINDOW, IMAGE_ICON, TITLE_WINDOW)
window.new_window()

window.new_rect(COTE_SCREEN_GAME, 0, BANNER_SIZE, COTE_SCREEN_GAME, GRAY)
window.new_rect(0, COTE_SCREEN_GAME, COTE_WINDOW, BANNER_SIZE, WHITE)

# 2- Load image for game
hero = GameImage(HERO_SOURCE, 0, 0, 32, 32, SIZE_SPRITE, SIZE_SPRITE)

# 3- Create and load maze
level = GameMaze('level/level1')
level.load_from_file()

# Create hero
mg = Hero('MacGyver', hero.surface, level, window.surface)

# Variable that continues the loop if = True, stops if = False
main_loop = True

# Main loop
while main_loop:

    # Loop Speed Limitation
    pygame.time.Clock().tick(30)

    # Display bg and maze in window
    window.new_rect(0, 0, COTE_SCREEN_GAME, COTE_SCREEN_GAME, BLACK)
    level.display(window.surface)
    nb_object_to_find = pygame.font.Font(None, 15)
    text_object = nb_object_to_find.render("Nombre d'objets à trouver : ", True, WHITE, GRAY)
    window.surface.blit(text_object, (455, 10))
    inventory = pygame.font.Font(None, 20)
    text_inventory = inventory.render(str(mg.Maze.Inventory), True, WHITE, GRAY)
    window.surface.blit(text_inventory, (585, 40))

    # Display hero
    mg.display()

    for event in pygame.event.get():  # We track the list of all the events received
        # If user quit the program stop or if the user presses a ESCAPE key
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            main_loop = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mg.move('right')
            elif event.key == K_LEFT:
                mg.move('left')
            elif event.key == K_DOWN:
                mg.move('down')
            elif event.key == K_UP:
                mg.move('up')

    # Refresh the display
    pygame.display.flip()

