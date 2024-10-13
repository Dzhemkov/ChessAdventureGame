from HelperFunctions.global_utilities import *

class MenuButton:
    def __init__(self, x, y, image, size_x, size_y):
        self.x = x
        self.y = y
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, size_x, size_y)
        self.clicked = False
        self.action = False

    def draw(self, surface):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                self.action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.x, self.y))

        return self.action