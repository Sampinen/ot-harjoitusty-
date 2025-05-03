"""This file contains all start menu buttons"""

import pygame


class MyButton():
    """Class for defining buttons and what they do"""

    def __init__(self, screen, text, x, y):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.clicked = False

    def draw(self):
        """Draws a button"""
        font = pygame.font.Font('freesansbold.ttf', 18)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.Rect((self.x, self.y), (150, 25))

        if self.check_click():
            pygame.draw.rect(self.screen, 'blue', button_rect, 0, 5)
            return True
        pygame.draw.rect(self.screen, 'yellow', button_rect, 0, 5)
        self.screen.blit(button_text, (self.x+3, self.y+3))
        return False

    def check_click(self):
        """Updates the variable if the button is clicked"""
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = button_rect = pygame.Rect(
            (self.x, self.y), (150, 25))
        if left_click and button_rect.collidepoint(mouse_pos):
            return True
        return False

    def change_screen(self):
        """Returns whether or not the button has been clicked"""
        return self.clicked
