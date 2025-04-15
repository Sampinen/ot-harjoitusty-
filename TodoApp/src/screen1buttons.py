import pygame


class MyButton():
    def __init__(self, screen, text, x, y, enabled, color='gray'):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.enabled = enabled
        self.draw()
        self.clicked = False

    def draw(self):
        font = pygame.font.Font('freesansbold.ttf', 18)

        if self.enabled:
            button_text = font.render(self.text, True, 'black')
            button_rect = pygame.rect.Rect((self.x, self.y), (150, 25))

            if self.check_click():
                pygame.draw.rect(self.screen, 'blue', button_rect, 0, 5)

            else:
                pygame.draw.rect(self.screen, 'yellow', button_rect, 0, 5)
            self.screen.blit(button_text, (self.x+3, self.y+3))
        else:
            pygame.draw.rect(self.screen, 'black', button_rect, 0, 5)

        # pygame.draw.rect(self.screen,'yellow',button_rect,0,5)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = button_rect = pygame.rect.Rect(
            (self.x, self.y), (150, 25))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

    def change_screen(self):
        return self.clicked
