"""Main file that runs the code"""

from screens.gamemenu import GameMenu

if __name__ == "__main__":
    StartMenu = GameMenu()
    StartMenu.start_menu()
    print("Program Closed")
