import os
import pygame

from HelperFunctions.button_boolean import GlobalBoolean

IMAGES = {
    'MAIN_MENU_IMAGE': pygame.image.load(os.path.join("Sprites", "Menu_sprites", "main_menu.png")),
    'START_GAME_IMAGE': pygame.image.load(os.path.join("Sprites", "Menu_sprites", "start_game.png")),
    'EXIT_IMAGE': pygame.image.load(os.path.join("Sprites", "Menu_sprites", "exit.png")),
    'GO_FULLSCREEN_IMAGE': pygame.image.load(os.path.join("Sprites", "Menu_sprites", "go_fullscreen.png"))
}

fullscreen = GlobalBoolean(True)
