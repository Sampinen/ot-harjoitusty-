# Example file showing a basic pygame "game loop"
import pygame
import pygame_widgets as pw
from pygame_widgets.button import Button
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

start_button = Button(
    screen, 100, 100, 300, 150, text='Aloita',
    fontSize=50, margin=20,
    inactiveColour=(122, 0, 0),
    pressedColour=(0, 255, 0), radius=20,
    onClick=lambda: print('Click')
)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    start_button.listen(events)
    start_button.draw()
    # flip() the display to put your work on screen

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()