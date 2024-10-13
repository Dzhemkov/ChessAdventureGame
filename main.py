import sys
from HelperFunctions.menu_button_func import *

pygame.display.set_caption('Pygame Boilerplate')


def main():
    pygame.init()

    screen_width = 2000
    screen_height = 1200
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    display = pygame.Surface(screen.get_size())
    clock = pygame.time.Clock()

    go_fullscreen = False

    while True:

        if not fullscreen.check_Boolean_On():
            start_game, go_fullscreen, exit_game = draw_main_menu(display)
        else:
            start_game, exit_game, _ = draw_main_menu(display)

        if exit_game:
            pygame.quit()
            sys.exit()
        if go_fullscreen:
            fullscreen.boolean_Make_On()
            GO_FULLSCREEN_BUTTON.action = False
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            #display = pygame.Surface(screen.get_size())
            go_fullscreen = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((screen_width, screen_height))
                    fullscreen.boolean_Make_Off()

        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
