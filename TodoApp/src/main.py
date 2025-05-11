"""Main file that runs the code"""

from screens.gamemenu import GameMenu
from screens.firstscreen import Screen1

if __name__ == "__main__":
    START = GameMenu().start_menu()
    if START:
        Screen1().run()

    print("Program Closed")
