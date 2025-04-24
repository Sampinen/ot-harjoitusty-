"""First screen of the game."""
#Pylint gives no-member error for valid pygame.event commands which is why disable no-member is used
import pygame
from texts import firstscreen_text as texts
from buttons import first_screen_buttons as buttons
from bottle_generator import BottleGenerator



class Screen1():
    """class that initializes the first game screen"""

    def __init__(self):
        """Initializes variables for the game"""
        pygame.init() # pylint: disable=no-member
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False
        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.name = ''
        self.active = False
        self.money = 0

    def get_money(self):
        """Meant for testing, returns the current amount of money"""
        return self.money

    def set_name(self, name):
        """Meant for testing, manually sets the name"""
        self.name = name

    def get_name(self):
        """Meant for testing, get the current name"""
        return self.name

    def draw_text(self, text, x, y):
        """Draws text on screen """
        img = self.font.render(text, True, 'black')
        screen_blit = self.screen.blit(img, (x, y))
        return screen_blit

    def input_rect(self, width):
        """Draws a rectangle for the input textbox"""
        rect = pygame.Rect(50, 50, max(100, width+10), 32)
        color = pygame.Color(
            'red') if self.active else pygame.Color('dark gray')
        return pygame.draw.rect(self.screen, color, rect, 2)

    def input_box(self):
        """renders the input text box"""
        return self.font.render(self.name, True, (255, 255, 255))

    def event_loop(self,events, input_rect, phase):
        """loops pygane events"""
        for event in events:
            if event.type == pygame.QUIT: # pylint: disable=no-member
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                if input_rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False

            if event.type == pygame.KEYDOWN: # pylint: disable=no-member
                if phase == 0:
                    if self.active:
                        if event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]
                        else:
                            self.name += event.unicode

                    if event.key == pygame.K_RETURN: # pylint: disable=no-member
                        return 1
        return 0

    def run(self):
        """Runs the game"""
        self.running = True
        self.screen.fill("white")
        input_rect = self.input_rect(0)
        phase = 0
        phases = set()
        bottle_generator = None
        while self.running:

            events = pygame.event.get()
            phase += self.event_loop(events,input_rect,phase)
            self.screen.fill("white")
            self.draw_text("Rahat(€): "+str(self.money),1000,10)
            phases.add(phase)
            if phase == 0:
                self.draw_text(
                    texts.welcome(), 10, 10)
                text_surface = self.font.render(self.name, True, 'black')
                input_rect = self.input_rect(text_surface.get_width())
                self.screen.blit(
                    text_surface, (input_rect.x+5, input_rect.y+5))
            if phase == 1:
                self.draw_text(
                    texts.say_hi(self.name), 10, 10)
                self.draw_text(
                    texts.backstory1(), 10, 30)
                self.draw_text(
                    texts.backstory2(), 10, 50)
                self.draw_text(
                    texts.backstory3(), 10, 70)
                self.draw_text(
                    texts.your_goal(), 10, 90
                )
                button1 =buttons.collect_bottles(self.screen,1)
                button2 =buttons.talk_to_friend(self.screen,1)
                if button1 != phase:
                    phase = button1
                else:
                    phase = button2

            if phase == 2:
                self.draw_text("Kerää pullo",10,10)
                if not bottle_generator:
                    bottle_generator = BottleGenerator()
                    bottle_generator.generate_bottles(self.screen)
                if bottle_generator.how_many_bottles() > 0:
                    self.money += bottle_generator.check_bottles()
                if 3 not in phases:
                    button2 = buttons.talk_to_friend(self.screen,2)
                    phase = button2
            if phase == 3:
                self.draw_text("Terve " +self.name+"! Mitä sinulle kuuluu?",10,10)
                if 2 not in phases:
                    button1 = buttons.collect_bottles(self.screen,3)
                    phase = button1
                
            if phase == 4:
                self.draw_text("Vaihe 4",10,10)
            pygame.display.update()

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit() # pylint: disable=no-member
