import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT,
                           K_DOWN, K_UP, K_RETURN)
from gamemaze.constants import (COTE_WINDOW, GRAY, WHITE, BLACK, HOME_TEXTS,
                                COTE_SCREEN_GAME, BANNER_SIZE, IMAGE_ICON,
                                TITLE_WINDOW, HERO_SOURCE, CASE_SIZE)
from gamemaze.models.game_image import GameImage
from gamemaze.models.game_window import GameWindow
from gamemaze.models.hero import Hero
from gamemaze.models.game_maze import GameMaze


class Game:
    def __init__(self):
        self.State = False

    def start_part(self):
        # Create window :
        window = GameWindow(COTE_WINDOW, COTE_WINDOW, IMAGE_ICON,
                            TITLE_WINDOW, BLACK)

        window.new_window()

        window.new_rect(COTE_SCREEN_GAME, 0, BANNER_SIZE,
                        COTE_SCREEN_GAME, GRAY)
        window.new_rect(0, COTE_SCREEN_GAME, COTE_WINDOW, BANNER_SIZE,
                        WHITE)

        for el in HOME_TEXTS:
            window.display_text(el[0], 30, BLACK, WHITE, 10, el[1])

        # Create and load maze
        level = GameMaze('level/level1')
        level.load_from_file()

        # Create hero
        hero = GameImage(HERO_SOURCE, 0, 0, 32, 32, CASE_SIZE,
                         CASE_SIZE)
        mg = Hero('MacGyver', hero.surface, level, window)

        # Variable that continues the loop if = True, stops if = False
        self.State = True

        # Main loop
        while self.State:

            # Loop Speed Limitation
            pygame.time.Clock().tick(30)

            # Display the game background in window
            window.new_rect(0, 0, COTE_SCREEN_GAME, COTE_SCREEN_GAME, BLACK)
            # Display maze in window
            level.display(window.surface)
            # Display inventory
            window.display_inventory(mg)
            # Display hero
            mg.display()

            for event in pygame.event.get():
                # If user quit the program or if the user presses a ESCAPE key
                if event.type == QUIT or (event.type == KEYDOWN
                                          and event.key == K_ESCAPE):
                    self.State = False
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        mg.move('right')
                    elif event.key == K_LEFT:
                        mg.move('left')
                    elif event.key == K_DOWN:
                        mg.move('down')
                    elif event.key == K_UP:
                        mg.move('up')

                    elif event.key == K_RETURN:
                        self.State = False
                        self.start_part()

            # Refresh the display
            pygame.display.flip()

