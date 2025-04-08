import pygame
from screen1buttons import MyButton
class Screen1():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False
        self.font = pygame.font.Font('freesansbold.ttf',18)
        self.user_text = ''
        self.active = False
    
    def draw_text(self,text,x,y):
        img = self.font.render(text, True, 'black')
        self.screen.blit(img, (x,y))
    def input_rect(self, width):

        rect= pygame.Rect(50,50,max(100,width+10),32)
        color = pygame.Color('red') if self.active else pygame.Color('dark gray')
        return pygame.draw.rect(self.screen,color,rect,2)

    def input_box(self):
        return self.font.render(self.user_text, True,(255,255,255))
    
    def run(self):
        #used code from pygame.org website as a layout
        self.running = True
        self.screen.fill("white")
        input_rect = self.input_rect(0)
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
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
                    if self.active:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                        else:
                            self.user_text +=event.unicode
            self.screen.fill("white")

            # fill the screen with a color to wipe away anything from last frameif
            

            #Pygame functions
            FUNCS = {}
            # RENDER YOUR GAME HERE
            self.draw_text("Tervetuloa peliin! Tässä pelissä tavoitteenasi on kerätä rahaa parta-agamaan. Mikä on sinun nimesi?", 10,10)
            text_surface = self.font.render(self.user_text, True,'black')
            input_rect = self.input_rect(text_surface.get_width())
            self.screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
            pygame.display.update()

            # flip() the display to put your work on screen

            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()
        return print("Program closed")
