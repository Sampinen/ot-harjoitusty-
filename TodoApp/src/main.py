# Example file showing a basic pygame "game loop"
import pygame
import pygame_widgets as pw
from pygame_widgets.button import Button
from gamemenu import GameMenu
# pygame setup

if __name__ == "__main__":
    StartMenu = GameMenu()
    StartMenu.start_menu()
    
