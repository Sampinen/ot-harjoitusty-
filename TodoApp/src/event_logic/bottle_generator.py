""" Collect bottles and earn money! Code for collect bottles (kerää pulloja) event"""
import random
import pygame
from entities.bottle import Bottle

class DrawBottle:
    """Class for defining bottles"""
    def __init__(self, screen, bottle_type, x=None,y=None):
        self.x = x if x is not None else random.randint(10,1200)
        self.y = y if y is not None else random.randint(30,700)
        self.clicked = False
        self.screen = screen
        self.bottle = Bottle(bottle_type)

    def draw(self):
        """Calls another function depending on bottle type"""
        if self.bottle.return_bottle_type() == "aluminium":
            self.aluminium_can()
        if self.bottle.return_bottle_type() == "large":
            self.large_plastic_bottle()
        if self.bottle.return_bottle_type() == "small":
            self.small_plastic_bottle()
        if self.bottle.return_bottle_type() == "glass":
            self.glass_bottle()

    def aluminium_can(self):
        """Creates an aluminum can"""
        image = pygame.image.load('src/event_logic/static/aluminium.png')
        image = pygame.transform.scale(image, (15, 20))
        self.screen.blit(image, (self.x, self.y))
        self.is_clicked()

    def large_plastic_bottle(self):
        """Creates a large plastic bottle"""
        image = pygame.image.load('src/event_logic/static/large.png')
        image = pygame.transform.scale(image, (20, 40))
        self.screen.blit(image, (self.x, self.y))
        self.is_clicked()

    def small_plastic_bottle(self):
        """Creates a small plastic bottle using an image"""
        image = pygame.image.load('src/event_logic/static/small.png')
        image = pygame.transform.scale(image, (10, 20))
        self.screen.blit(image, (self.x, self.y))
        self.is_clicked()

    def glass_bottle(self):
        """Creates a glass bottle"""
        image = pygame.image.load('src/event_logic/static/glass.png')
        image = pygame.transform.scale(image, (15, 30))
        self.screen.blit(image, (self.x, self.y))
        self.is_clicked()

    def is_clicked(self,debug=False):
        """Draws a button"""
        if self.check_click() or debug:
            return self.bottle.return_deposit()
        return 0

    def check_click(self,debug=False):
        """Updates the variable if the button is clicked"""
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = button_rect = pygame.Rect(
            (self.x, self.y), (150, 25))
        if left_click and button_rect.collidepoint(mouse_pos) or debug:
            return True
        return False

class BottleGenerator:
    """ A class for generating random bottles"""
    def __init__(self):
        self.bottles = []

    def generate_bottles(self,screen):
        """Generates random amount of bottles to collect"""
        for _ in range(0,random.randint(1,3)):
            can = DrawBottle(screen,"aluminium")
            self.bottles.append(can)
        for _ in range(0, random.randint(1,3)):
            bottle = DrawBottle(screen, "large")
            self.bottles.append(bottle)
        for _ in range(0, random.randint(1,3)):
            bottle = DrawBottle(screen, "small")
            self.bottles.append(bottle)
        for _ in range(0, random.randint(1,3)):
            bottle = DrawBottle(screen, "glass")
            self.bottles.append(bottle)
    def is_clicked(self,bottle,debug=False):
        """If bottle is clicked, remove from bottle list and return deposit money"""
        clicked = bottle.is_clicked() if not debug else bottle.is_clicked(debug=True)
        if clicked != 0:
            self.bottles.remove(bottle)
            return clicked
        return 0

    def check_bottles(self,debug=False):
        """Loop that checks if bottle is clicked """
        bottle= self.bottles[0]
        bottle.draw()
        return self.is_clicked(bottle) if not debug else self.is_clicked(bottle, debug=True)

    def how_many_bottles(self):
        """ Checks how many bottles are in the list """
        return len(self.bottles)
    def bottle_list(self):
        """Returns bottle list saved in the __init__ function"""
        return self.bottles
