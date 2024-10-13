from HelperFunctions.global_utilities import *
from HelperFunctions.menu_buttons import MenuButton

EXIT_BUTTON = MenuButton(250 - IMAGES['EXIT_IMAGE'].get_width() / 2, 450 - IMAGES['EXIT_IMAGE'].get_height() / 2,
                         IMAGES['EXIT_IMAGE'], IMAGES['EXIT_IMAGE'].get_width(), IMAGES['EXIT_IMAGE'].get_height())

START_GAME_BUTTON = MenuButton(250 - IMAGES['START_GAME_IMAGE'].get_width() / 2,
                               300 - IMAGES['START_GAME_IMAGE'].get_height() / 2,
                               IMAGES['START_GAME_IMAGE'], IMAGES['START_GAME_IMAGE'].get_width(),
                               IMAGES['START_GAME_IMAGE'].get_height())

MAIN_MENU_BUTTON = MenuButton(250 - IMAGES['MAIN_MENU_IMAGE'].get_width() / 2,
                              375 - IMAGES['MAIN_MENU_IMAGE'].get_height() / 2,
                              IMAGES['MAIN_MENU_IMAGE'], IMAGES['MAIN_MENU_IMAGE'].get_width(),
                              IMAGES['MAIN_MENU_IMAGE'].get_height())

GO_FULLSCREEN_BUTTON = MenuButton(0, 0,
                              IMAGES['GO_FULLSCREEN_IMAGE'], IMAGES['GO_FULLSCREEN_IMAGE'].get_width(),
                              IMAGES['GO_FULLSCREEN_IMAGE'].get_height())


def draw_main_menu(display):
    START_GAME_BUTTON.draw(display)
    EXIT_BUTTON.draw(display)

    if not fullscreen.check_Boolean_On():
        GO_FULLSCREEN_BUTTON.draw(display)
        return START_GAME_BUTTON.action, GO_FULLSCREEN_BUTTON.action, EXIT_BUTTON.action
    else:
        return START_GAME_BUTTON.action, EXIT_BUTTON.action, False
