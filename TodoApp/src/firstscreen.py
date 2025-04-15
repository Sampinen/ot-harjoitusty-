"""First screen of the game"""

import pygame


class Screen1():
    """class that initializes the first game screen"""

    def __init__(self):
        """Initializes variables for the game"""
        pygame.init()
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

    def say_hi(self):
        """Says nice to meet you and the players name based on text input"""
        return "Hauska tavata "+self.name+"!"

    def welcome(self):
        """The text that is printed when the screen is first opened"""
        return "Tervetuloa peliin! Tässä pelissä tavoitteenasi on kerätä rahaa parta-agamaan. Mikä on sinun nimesi?"

    def backstory1(self):
        """First line of text that is printed when you have written your name"""
        return "Siitä asti kun näit viisivuotiaana lemmikkikaupassa parta-agaman, olet tahtonut sellaisen lemmikiksi."

    def backstory2(self):
        """Second line of text that is printed when you have written your name"""
        return "Vanhempasi eivät kuitenkaan olleet ideasta tohkeissaan ja et koskaan saanut sellaista lapsena."

    def backstory3(self):
        """Third line of text that is printed when you have written your name"""
        return "Nyt 20-vuoden jälkeen olet vihdoin päättänyt kerätä rahaa ostaa sellaisen syntymäpäivälahjaksesi."

    def your_goal(self):
        """Fourth line of text that is printed when you have written your name"""
        return "Tavoitteenasi on kerätä 200 euroa. Onnea peliin!"

    def draw_text(self, text, x, y):
        """Draws text on screen """
        img = self.font.render(text, True, 'black')
        self.screen.blit(img, (x, y))

    def input_rect(self, width):
        """Draws a rectangle for the input textbox"""
        rect = pygame.Rect(50, 50, max(100, width+10), 32)
        color = pygame.Color(
            'red') if self.active else pygame.Color('dark gray')
        return pygame.draw.rect(self.screen, color, rect, 2)

    def input_box(self):
        """renders the input text box"""
        return self.font.render(self.name, True, (255, 255, 255))

    def run(self):
        """Runs the game"""
        self.running = True
        self.screen.fill("white")
        input_rect = self.input_rect(0)
        phase = 0
        while self.running:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        self.active = True
                    else:
                        self.active = False

                if event.type == pygame.KEYDOWN:
                    if phase == 0:
                        if self.active:

                            if event.key == pygame.K_BACKSPACE:
                                self.name = self.name[:-1]
                            else:
                                self.name += event.unicode

                        if event.key == pygame.K_RETURN:
                            phase = 1
            self.screen.fill("white")

            if phase == 0:
                self.draw_text(
                    self.welcome(), 10, 10)
                text_surface = self.font.render(self.name, True, 'black')
                input_rect = self.input_rect(text_surface.get_width())
                self.screen.blit(
                    text_surface, (input_rect.x+5, input_rect.y+5))
            if phase == 1:
                self.draw_text(
                    self.say_hi(), 10, 10)
                self.draw_text(
                    self.backstory1(), 10, 30)
                self.draw_text(
                    self.backstory2(), 10, 50)
                self.draw_text(
                    self.backstory3(), 10, 70)
                self.draw_text(
                    self.your_goal(), 10, 90
                )
            pygame.display.update()

            pygame.display.update()

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        return print("Program closed")
