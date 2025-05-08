"""First screen of the game."""
#Pylint gives no-member error for valid pygame.event commands which is why disable no-member is used
import pygame
import draw.draw_text as texts
from buttons import first_screen_buttons as buttons
from event_logic.bottle_generator import BottleGenerator
from entities.user import User
import draw.draw_images as drawimg

class Screen1():
    """class that initializes the first game screen"""

    def __init__(self):
        """Initializes variables for the game"""
        pygame.init() # pylint: disable=no-member
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False
        self.user = User()
        self.active = False

    def input_rect(self, width):
        """Draws a rectangle for the input textbox"""
        rect = pygame.Rect(50, 75, max(100, width+10), 32)
        color = pygame.Color(
            'red') if self.active else pygame.Color('dark gray')
        return pygame.draw.rect(self.screen, color, rect, 2)

    def input_box(self):
        """renders the input text box"""
        font =pygame.font.Font('freesansbold.ttf', 18)
        return font.render(self.user.return_name(), True, (255, 255, 255))

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
                            self.user.remove_letter()
                        else:
                            self.user.add_letter(event.unicode)

                    if event.key == pygame.K_RETURN: # pylint: disable=no-member
                        return 1
        return 0

    def run(self):
        """Runs the game"""
        self.running = True
        self.screen.fill("white")
        input_rect = self.input_rect(0)
        phase = 0
        step="one"
        phases = set()
        bottle_generator = None
        while self.running:
            events = pygame.event.get()
            phase += self.event_loop(events,input_rect,phase)
            drawimg.draw_background(self.screen)
            drawimg.draw_trash_can(self.screen)
            texts.print_money(self.screen,str(self.user.return_money()))
            phases.add(phase)
            if phase == 0:
                self.phase_zero()
            if phase == 1:
                phase = self.phase_one(phase)
            if phase == 2:
                phase2 = self.phase_two(phase, phases, bottle_generator)
                phase = phase2[1]
                bottle_generator = phase2[0]
            if phase == 3:
                phase3 = self.phase_three(phase,phases,step)
                phase = phase3[0]
                step = phase3[1]
                print(step)
            if phase == 4:
                self.phase_four()
            pygame.display.update()

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit() # pylint: disable=no-member

    def phase_zero(self):
        """Determines what happens during the zero phase"""
        texts.draw_phase0_1(self.screen)
        font = pygame.font.Font('freesansbold.ttf', 18)
        text_surface = font.render(self.user.return_name(), True, 'black')
        drawimg.draw_bottles(self.screen)
        input_rect = self.input_rect(text_surface.get_width())
        self.screen.blit(
            text_surface, (input_rect.x+5, input_rect.y+5))

    def phase_one(self,phase):
        """Determines what happens during the first phase"""
        texts.draw_phase1_1(self.screen,self.user.return_name())
        button1 =buttons.collect_bottles(self.screen,1)
        drawimg.draw_bottles(self.screen)
        drawimg.draw_character2(self.screen)
        button2 =buttons.talk_to_friend(self.screen,1)
        if button1 != phase:
            return button1
        return button2

    def phase_two(self,phase,phases,bottle_generator):
        """Determines what happens during phase two"""
        texts.draw_phase2(self.screen)
        if not bottle_generator:
            bottle_generator = BottleGenerator()
            bottle_generator.generate_bottles(self.screen)
        if bottle_generator.how_many_bottles() > 0:
            self.user.update_money(bottle_generator.check_bottles())
        if 3 not in phases:
            button2 = buttons.talk_to_friend(self.screen,2)
            drawimg.draw_character2(self.screen)
            return bottle_generator, button2
        return bottle_generator, phase

    def phase_three(self,phase, phases,step):
        """determines what happens during phase three"""
        drawimg.draw_character2(self.screen)
        if step == "one":
            #"""Have we met before?"""
            texts.draw_phase3_1(self.screen)
            answer1 =buttons.yes_i_know_you(self.screen,step)
            answer2= buttons.no_we_have_not_met_before(self.screen,step)
            print(answer1)
            if answer1 != step:
                step = answer1
            elif answer2 != step:
                step = answer2
        elif step == "two":
            #Oh now I remember you
            texts.draw_phase3_2(self.screen)
            answer1 = buttons.could_i_have_some_money(self.screen,step)
            answer2= buttons.nice_weather(self.screen,step)
            answer3= buttons.give_me_money(self.screen,step)
            if answer1 != step:
                step = answer1
            elif answer2 != step:
                step= answer2
            elif answer3 != step:
                step = answer3
        elif step == "three":
            #"""Why are you here?"""
            texts.draw_phase3_3(self.screen)
            answer1 =buttons.give_me_money(self.screen,step)
            answer2 =buttons.nice_weather(self.screen,step)
            if answer1 != step:
                step = answer1
            elif answer2 !=step:
                step = answer2
        elif step == "four":
            #"""Why are you asking money from a stranger?"""
            texts.draw_phase3_4(self.screen)
            drawimg.draw_character1(self.screen)
        elif step == "five":
            #"""I'm not giving money for free!"""
            texts.draw_phase3_5(self.screen)
            drawimg.draw_character1(self.screen)
        elif step == "six":
            #"""I will give money if you feed birds"""
            texts.draw_phase3_6(self.screen)
            drawimg.draw_bird(self.screen)
            buttons.feed_the_birds(self.screen,phase)
        elif step == "seven":
            #"""It was nice to meet you"""
            texts.draw_phase3_7(self.screen)
            drawimg.draw_character1(self.screen)
            drawimg.draw_bird(self.screen)
        if 2 not in phases:
            drawimg.draw_bottles(self.screen)
            button1 = buttons.collect_bottles(self.screen,3)
            return button1,step
        if 4 not in phases:
            drawimg.draw_character1(self.screen)
        return phase, step
    def phase_four(self):
        """determines what happens during phase four"""
