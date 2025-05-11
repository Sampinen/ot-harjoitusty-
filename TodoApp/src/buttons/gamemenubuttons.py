"""This file contains all start menu buttons"""

import pygame


class MyButton():
    """Class for defining buttons and what they do"""

    def __init__(self, screen, text):
        self.screen = screen
        self.text = text
        self.clicked = False

    def draw(self,debug =False):
        """Draws a button"""
        font = pygame.font.Font('freesansbold.ttf', 50)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.Rect((500, 200), (175, 60))

        if self.check_click() or debug:
            pygame.draw.rect(self.screen, 'blue', button_rect, 0, 5)
            return True
        pygame.draw.rect(self.screen, 'green', button_rect, 0, 5)
        self.screen.blit(button_text, (510, 210))
        return False

    def check_click(self, debug=False):
        """Updates the variable if the button is clicked"""
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = button_rect = pygame.Rect(
            (500, 200), (175, 60))
        if left_click and button_rect.collidepoint(mouse_pos) or debug:
            return True
        return False

    def change_screen(self):
        """Returns whether or not the button has been clicked"""
        return self.clicked
