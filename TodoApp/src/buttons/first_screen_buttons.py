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

    def draw(self, current_phase, output, debug=False):
        """Draws a button"""
        font = pygame.font.Font('freesansbold.ttf', 18)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.Rect((self.x, self.y), (250, 25))

        if self.check_click() or debug:
            pygame.draw.rect(self.screen, 'blue', button_rect, 0, 5)
            return output
        pygame.draw.rect(self.screen, 'yellow', button_rect, 0, 5)
        self.screen.blit(button_text, (self.x+3, self.y+3))
        return current_phase

    def check_click(self, debug=False):
        """Updates the variable if the button is clicked"""
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = button_rect = pygame.Rect(
            (self.x, self.y), (150, 25))
        if left_click and button_rect.collidepoint(mouse_pos) or debug:
            return True
        return False


def collect_bottles(screen,current_phase, debug=False):
    """Creates a button for a specific event by calling MyButton class"""
    button = MyButton(screen, "Mene keräämään pulloja", 50, 150)
    return button.draw(current_phase,2) if not debug else button.draw(current_phase,2,debug=True)

def talk_to_friend(screen,current_phase, debug=False):
    """Creates a button for a specific event by calling MyButton class"""
    button = MyButton(screen, "Mene puhumaan kaverille", 50, 200)
    return button.draw(current_phase,3) if not debug else button.draw(current_phase,3, debug=True)
