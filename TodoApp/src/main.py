# Example file showing a basic pygame "game loop"
import pygame
from gamemenu import GameMenu
from firstscreen import Screen1
# pygame setup

if __name__ == "__main__":
    StartMenu = GameMenu()
    menu =StartMenu.start_menu()
    if menu == True:
        Screen1()
    else:
        print("Program Closed")
