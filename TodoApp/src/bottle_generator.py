import random
import pygame

class Bottle:
    def __init__(self, screen, bottle_type, x=None,y=None):
        self.x = x if x is not None else random.randint(10,1200)
        self.y = y if y is not None else random.randint(30,700)
        self.clicked = False
        self.screen = screen
        self.deposit = None
        self.bottle_type = bottle_type
    
    def draw(self):
        """Calls another function depending on bottle type"""
        if self.bottle_type == "aluminium":
            self.aluminium_can()
        if self.bottle_type == "large":
            self.large_plastic_bottle()
        if self.bottle_type == "small":
            self.small_plastic_bottle()
        if self.bottle_type == "glass":
            self.glass_bottle()
        
    def aluminium_can(self):
        """Creates an aluminum can"""
        rect = pygame.Rect(self.x, self.y, 10, 15)
        color = pygame.Color('green')
        self.deposit = 0.15
        pygame.draw.rect(self.screen, color, rect, 2)
        self.is_clicked()

    def large_plastic_bottle(self):
        """Creates a large plastic bottle"""
        rect = pygame.Rect(self.x, self.y, 15, 40)
        color = pygame.Color('blue')
        self.deposit = 0.40
        pygame.draw.rect(self.screen, color, rect, 2)
        self.is_clicked()

    def small_plastic_bottle(self):
        """Creates a small plastic bottle"""
        rect = pygame.Rect(self.x, self.y, 10, 20)
        color = pygame.Color('red')
        self.deposit =0.20
        pygame.draw.rect(self.screen, color, rect, 2)
        self.is_clicked()

    def glass_bottle(self):
        """Creates a glass bottle"""
        rect = pygame.Rect(self.x, self.y, 10, 30)
        color = pygame.Color('gray')
        self.deposit = 0.10
        pygame.draw.rect(self.screen, color, rect, 2)
        self.is_clicked()
    
    def is_clicked(self):
        """Draws a button"""
        if self.check_click():
            return self.deposit
        return 0

    def check_click(self):
        """Updates the variable if the button is clicked"""
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = button_rect = pygame.Rect(
            (self.x, self.y), (150, 25))
        if left_click and button_rect.collidepoint(mouse_pos):
            return True
        return False

    
class BottleGenerator:
    """ A class for generating random bottles"""
    def __init__(self):
        self.bottles = []
    
    def generate_bottles(self,screen):
        """Generates random amount of bottles to collect"""
        for _ in range(0,random.randint(1,3)):
            can = Bottle(screen,"aluminium")
            self.bottles.append(can)
        for _ in range(0, random.randint(0,3)):
            bottle = Bottle(screen, "large")
            self.bottles.append(bottle)
        for _ in range(0, random.randint(1,3)):
            bottle = Bottle(screen, "small")
            self.bottles.append(bottle)
        for _ in range(0, random.randint(1,3)):
            bottle = Bottle(screen, "glass")
            self.bottles.append(bottle)
    def is_clicked(self,bottle):
        clicked = bottle.is_clicked()
        if clicked != 0:
            self.bottles.remove(bottle)
            return clicked
        return 0

    def check_bottles(self):
        for bottle in self.bottles:
            bottle.draw()
            return self.is_clicked(bottle)
    
    def how_many_bottles(self):
        return len(self.bottles)
