import pygame
import pygame_widgets
from pygame_widgets.button import Button

class MyButton():
    def __init__(self):
        None
    
    def create_button(self, win, x=100, y=100, width=300, height=150, text="", fontSize=50, margin=20, inactivecolour=(200, 50, 0), hoverColour=(150, 0, 0), pressedcolour=(0, 200, 20), radius=20, onClick=lambda: print('Click')):
        button = Button(
            # Mandatory Parameters
            win,  # Surface to place button on
            x,  # X-coordinate of top left corner
            y,  # Y-coordinate of top left corner
            width,  # Width
            height,  # Height

            # Optional Parameters
            text=text,  # Text to display
            fontSize=fontSize,  # Size of font
            margin=margin,  # Minimum distance between text/image and edge of button
            inactiveColour=inactivecolour,  # Colour of button when not being interacted with
            hoverColour=hoverColour,  # Colour of button when being hovered over
            pressedColour=pressedcolour,  # Colour of button when being clicked
            radius=radius,  # Radius of border corners (leave empty for not curved)
            onClick=onClick  # Function to call when clicked on
        )
        return button



class GameMenu():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = False
    def start_menu(self):
        self.running = True
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("gray")

            # RENDER YOUR GAME HERE
            start_button = MyButton().create_button(self.screen, 100, 100, 300, 150, 'Aloita',50, 20,(122, 0, 0),(122, 255, 0) ,(0, 255, 0), 20,lambda: print('Click'))
            start_button.listen(events)
            start_button.draw()
            pygame.display.update()
            # flip() the display to put your work on screen

            pygame.display.flip()
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()
        return print("Program closed")
    
    def IsGameRunning(self):
        return self.running
    
    def CloseGame(self):
        self.running = False
        return self.running