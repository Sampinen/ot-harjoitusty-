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
    button = MyButton(screen, "Mene keräämään pulloja", 390, 560)
    return button.draw(current_phase,2) if not debug else button.draw(current_phase,2,debug=True)

def talk_to_friend(screen,current_phase, debug=False):
    """Creates a button for a specific event by calling MyButton class"""
    button = MyButton(screen, "Puhu mummolle", 1050, 350)
    return button.draw(current_phase,3) if not debug else button.draw(current_phase,3, debug=True)

def yes_i_know_you(screen,current_phase, debug=False):
    """step one"""
    button = MyButton(screen, "Kyllä,olemme tavanneet", 100, 100)
    return button.draw(current_phase,"two") if not debug else button.draw(current_phase,"two", debug=True)

def no_we_have_not_met_before(screen,current_phase, debug=False):
    """step one"""
    button = MyButton(screen, "En usko tavanneesi sinua aiemmin.", 100, 150)
    return button.draw(current_phase,"three") if not debug else button.draw(current_phase,"three", debug=True)

def give_me_money(screen,current_phase, debug=False):
    """step two and three"""
    button = MyButton(screen, "Anna rahaa pliis", 100, 200)
    return button.draw(current_phase,"five") if not debug else button.draw(current_phase,"five", debug=True)

def could_i_have_some_money(screen,current_phase, debug=False):
    """step two"""
    button = MyButton(screen, "Onko mitään tapaa, jolla voisin tienata rahaa?", 100, 250)
    return button.draw(current_phase,"six") if not debug else button.draw(current_phase,"six", debug=True)

def nice_weather(screen,current_phase, debug=False):
    """step two and three"""
    button = MyButton(screen, "Onpas täällä kaunis sää", 100, 300)
    return button.draw(current_phase,"seven") if not debug else button.draw(current_phase,"seven", debug=True)


def talk_to_vampire(screen,current_phase,debug=False):
    """step seven"""
    button = MyButton(screen, "Puhu miehelle", 600, 300)
    return button.draw(current_phase,3) if not debug else button.draw(current_phase,3, debug=True)

def feed_the_birds(screen,current_phase,debug=False):
    """step seven"""
    button = MyButton(screen, "Ruoki lintuja", 100, 500)
    return button.draw(current_phase,3) if not debug else button.draw(current_phase,3, debug=True)